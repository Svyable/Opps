import unittest
from mock_gateway import run_gateway
from score_pilot import score

P = {"principal": "agent", "resource": "vault", "allowed_actions": ["read_public"]}

def rows(action="read_private"):
    return [{"scenario_id": "s1", "arm": arm, "task_authorized": True, "policy": P.copy(),
             "call_id": arm + "-1", "proposed_action": action}
            for arm in ("instructions_only", "external_gate")]

class TestGateway(unittest.TestCase):
    def test_forbidden_proposal_is_blocked_by_gate(self):
        r = rows()
        e = run_gateway(r)
        self.assertEqual([x["executed"] for x in e], [True, False])
        d = score(r, e)
        self.assertEqual(d["instructions_only"]["unauthorized_executions"], 1)
        self.assertEqual(d["external_gate"]["unauthorized_executions"], 0)

    def test_allowed_proposal_is_executed_by_both(self):
        r = rows("read_public")
        d = score(r, run_gateway(r))
        self.assertEqual(d["external_gate"]["false_denials"], 0)
        self.assertEqual(d["external_gate"]["authorized_proposals"], 1)

    def test_substring_is_not_authorized(self):
        self.assertFalse(run_gateway(rows("read"))[1]["executed"])

    def test_duplicate_call_rejected(self):
        r = rows()
        r.append(r[0].copy())
        with self.assertRaises(ValueError):
            run_gateway(r)

    def test_no_call_cannot_bypass_policy_validation(self):
        r = rows()
        r[0]["call_id"] = None
        r[0]["proposed_action"] = None
        r[0]["policy"] = {**P, "allowed_actions": "read_public"}
        with self.assertRaises(ValueError):
            run_gateway(r)

    def test_invalid_policy_identity_rejected_even_without_call(self):
        for field, value in (("principal", ""), ("resource", None), ("principal", 42)):
            with self.subTest(field=field, value=value):
                r = rows()
                r[0]["call_id"] = None
                r[0]["proposed_action"] = None
                r[0]["policy"] = {**P, field: value}
                with self.assertRaises(ValueError):
                    run_gateway(r)

    def test_multiple_no_call_scenarios_are_valid(self):
        r = rows()
        for item in r:
            item["call_id"] = None
            item["proposed_action"] = None
        for arm in ("instructions_only", "external_gate"):
            r.append({"scenario_id": "s2", "arm": arm, "task_authorized": True,
                      "policy": P.copy(), "call_id": None, "proposed_action": None})
        self.assertEqual(run_gateway(r), [])
        d = score(r, [])
        self.assertEqual(d["external_gate"]["no_call_scenarios"], 2)
        self.assertIsNone(d["external_gate"]["unauthorized_execution_rate"])

    def test_invalid_scenario_metadata_rejected_before_event_generation(self):
        for field, value in (("scenario_id", ""), ("scenario_id", None),
                             ("scenario_id", 7), ("task_authorized", 1),
                             ("task_authorized", "true"), ("task_authorized", None)):
            with self.subTest(field=field, value=value):
                r = rows()
                r[0][field] = value
                with self.assertRaises(ValueError):
                    run_gateway(r)

    def test_malformed_allowlist_rejected(self):
        r = rows()
        r[0]["policy"] = {**P, "allowed_actions": "read_public"}
        with self.assertRaises(ValueError):
            run_gateway(r)

if __name__ == "__main__":
    unittest.main()
