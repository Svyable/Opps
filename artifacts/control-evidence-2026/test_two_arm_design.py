#!/usr/bin/env python3
import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('two_arm_design', Path(__file__).with_name('two_arm_design.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def fixtures():
    b = {'schema_version': 1, 'dataset_id': 'synthetic-demo', 'source_sha256': 'a' * 64, 'case_count': 12}
    cases = [{'review_id': f'id-{i:02}', 'claim_type': ['action_completed', 'approval_before_action', 'alert_delivered'][i % 3],
              'scope_id': 'test', 'action_id': 'fake', 'args_digest': 'digest', 'coverage': 'complete',
              'coverage_writer': 'independent', 'events': []} for i in range(12)]
    packet = {**b, 'packet_type': 'reviewer_blinded', 'cases': cases}
    narratives = {c['review_id']: f'Agent claims synthetic action for {c["review_id"]}.' for c in cases}
    key = {**b, 'packet_type': 'PRIVATE_LABEL_KEY', 'labels': [
        {'review_id': c['review_id'], 'case_id': f'private-{i}', 'expected_verdict': ['supported', 'refuted', 'insufficient_evidence'][i % 3]}
        for i, c in enumerate(cases)]}
    return packet, narratives, key


class TwoArmTests(unittest.TestCase):
    def setUp(self):
        self.packet, self.narratives, self.key = fixtures()
        self.secret = b's' * 32

    def test_balanced_and_each_case_once_per_reviewer(self):
        packets, assignments = m.allocate(self.packet, self.narratives, self.secret)
        self.assertEqual(len(assignments['assignments']), 24)
        for p in packets.values():
            self.assertEqual(len(p['cases']), 12)
            self.assertEqual(len(set(x['review_id'] for x in p['cases'])), 12)
            self.assertEqual(sum(x['arm'] == 'narrative_plus_receipts' for x in p['cases']), 6)
        for rid in self.narratives:
            self.assertEqual({x['arm'] for x in assignments['assignments'] if x['review_id'] == rid}, set(m.ARMS))

    def test_no_receipt_leakage_in_narrative_only(self):
        packets, _ = m.allocate(self.packet, self.narratives, self.secret)
        for p in packets.values():
            for c in p['cases']:
                if c['arm'] == 'narrative_only':
                    self.assertTrue(set(c).isdisjoint(m.EVIDENCE_FIELDS))
                else:
                    self.assertTrue(set(m.EVIDENCE_FIELDS).issubset(c))
                self.assertNotIn('expected_verdict', c)

    def test_determinism(self):
        self.assertEqual(m.allocate(self.packet, self.narratives, self.secret), m.allocate(self.packet, self.narratives, self.secret))

    def test_reject_missing_narrative(self):
        n = dict(self.narratives); n.pop('id-00')
        with self.assertRaises(ValueError): m.allocate(self.packet, n, self.secret)

    def test_reject_duplicate_ids(self):
        p = copy.deepcopy(self.packet); p['cases'][1]['review_id'] = p['cases'][0]['review_id']
        with self.assertRaises(ValueError): m.allocate(p, self.narratives, self.secret)

    def test_reject_label_leak(self):
        p = copy.deepcopy(self.packet); p['cases'][0]['expected_verdict'] = 'supported'
        with self.assertRaises(ValueError): m.allocate(p, self.narratives, self.secret)

    def test_reject_weak_secret(self):
        with self.assertRaises(ValueError): m.allocate(self.packet, self.narratives, b'weak')

    def test_summarize_all_reference_agree(self):
        _, a = m.allocate(self.packet, self.narratives, self.secret)
        truth = {x['review_id']: x['expected_verdict'] for x in self.key['labels']}
        responses = {r: {x['review_id']: truth[x['review_id']] for x in a['assignments'] if x['reviewer_id'] == r} for r in ('R1','R2')}
        s = m.summarize(a, self.key, responses)
        self.assertEqual([s['by_arm'][arm]['reference_agreement'] for arm in m.ARMS], [12, 12])
        self.assertFalse(s['reference_is_ground_truth'])

    def test_summarize_reject_missing(self):
        _, a = m.allocate(self.packet, self.narratives, self.secret)
        responses = {r: {x['review_id']: 'no_decision' for x in a['assignments'] if x['reviewer_id'] == r} for r in ('R1','R2')}
        responses['R1'].pop('id-00')
        with self.assertRaises(ValueError): m.summarize(a, self.key, responses)

    def test_summarize_reject_wrong_binding(self):
        _, a = m.allocate(self.packet, self.narratives, self.secret)
        key = copy.deepcopy(self.key); key['source_sha256'] = 'b' * 64
        with self.assertRaises(ValueError): m.summarize(a, key, {})

    def test_reject_duplicate_assignment(self):
        _, a = m.allocate(self.packet, self.narratives, self.secret)
        a['assignments'][1]['arm'] = a['assignments'][0]['arm']
        responses = {r: {x['review_id']: 'no_decision' for x in a['assignments'] if x['reviewer_id'] == r} for r in ('R1','R2')}
        with self.assertRaises(ValueError): m.summarize(a, self.key, responses)


if __name__ == '__main__':
    unittest.main()
