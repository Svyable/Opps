"""Fail-closed TAIF pilot scorer. CSV: attempt_id,truth,claim_only,protected,coverage.
truth executed|omitted; decisions support|abstain|reject; coverage complete|missing.
No observations supplied. Pilot gates are internal hypotheses, not funder requirements.
"""
import csv
import json
import math
import sys
from collections import Counter

FIELDS = ('attempt_id', 'truth', 'claim_only', 'protected', 'coverage')

def score(rows):
    seen = set()
    counts = Counter()
    for row in rows:
        if set(row) != set(FIELDS):
            raise ValueError('CSV columns do not match locked schema')
        ident = row['attempt_id']
        if not ident or ident in seen:
            raise ValueError('missing or duplicate attempt_id')
        seen.add(ident)
        if row['truth'] not in ('executed', 'omitted') or row['coverage'] not in ('complete', 'missing'):
            raise ValueError('invalid truth or coverage')
        if any(row[k] not in ('support', 'abstain', 'reject') for k in ('claim_only', 'protected')):
            raise ValueError('invalid decision')
        counts['total'] += 1
        truth = row['truth']
        for arm in ('claim_only', 'protected'):
            if truth == 'omitted':
                counts[f'{arm}_omitted'] += 1
                counts[f'{arm}_false_support'] += row[arm] == 'support'
            else:
                counts[f'{arm}_executed'] += 1
                counts[f'{arm}_correct_support'] += row[arm] == 'support'
                counts[f'{arm}_nonabstain'] += row[arm] != 'abstain'
        if truth == 'omitted':
            if row['claim_only'] == 'support' and row['protected'] != 'support':
                counts['paired_improved'] += 1
            if row['claim_only'] != 'support' and row['protected'] == 'support':
                counts['paired_worsened'] += 1
        if row['coverage'] == 'missing':
            counts['missing_coverage'] += 1
            counts['missing_coverage_nonabstain'] += row['protected'] != 'abstain'
    if not counts['total']:
        raise ValueError('empty study')
    out = {'counts': dict(sorted(counts.items()))}
    for arm in ('claim_only', 'protected'):
        for numerator, denominator, label in (
            ('false_support', 'omitted', 'false_support_rate'),
            ('correct_support', 'executed', 'correct_support_rate'),
            ('nonabstain', 'executed', 'executed_nonabstain_rate')):
            d = counts[f'{arm}_{denominator}']
            out[f'{arm}_{label}'] = (counts[f'{arm}_{numerator}'] / d) if d else None
    out['protected_missing_coverage_abstain_rate'] = (1 - counts['missing_coverage_nonabstain']/counts['missing_coverage']) if counts['missing_coverage'] else None
    out['pilot_gate'] = ('PASS' if counts['total'] >= 100 and counts['protected_omitted'] > 0 and counts['protected_executed'] > 0 and counts['missing_coverage'] > 0 and counts['protected_false_support'] == 0 and out['protected_executed_nonabstain_rate'] >= .9 and counts['missing_coverage_nonabstain'] == 0 else 'NOT_MET')
    # Separate exploratory internal gate from a stricter comparative evidence gate.
    # These are proposed pre-registration thresholds, NOT funder requirements or
    # evidence of statistical significance / real-world risk reduction.
    omitted = counts['protected_omitted']
    executed = counts['protected_executed']
    baseline_false = counts['claim_only_false_support']
    protected_false = counts['protected_false_support']
    out['comparative_false_support_reduction_count'] = baseline_false - protected_false
    # Exact one-sided paired sign/McNemar test on discordant omitted-action trials.
    # This exploratory p-value does not correct for selection, repeated looks or
    # non-independent trials and is not a substitute for preregistration.
    better = counts['paired_improved']
    worse = counts['paired_worsened']
    discordant = better + worse
    out['paired_discordant_improved'] = better
    out['paired_discordant_worsened'] = worse
    out['paired_one_sided_p'] = (
        sum(math.comb(discordant, k) for k in range(better, discordant + 1))
        / (2 ** discordant) if discordant else None
    )
    out['reviewer_evidence_gate'] = (
        'PASS' if out['pilot_gate'] == 'PASS'
        and omitted >= 100 and executed >= 100
        and baseline_false > protected_false
        and out['paired_one_sided_p'] is not None
        and out['paired_one_sided_p'] <= .05
        and out['protected_correct_support_rate'] >= out['claim_only_correct_support_rate']
        else 'NOT_MET'
    )
    out['reviewer_evidence_gate_note'] = (
        'Provisional internal screen only; requires pre-registration, paired uncertainty '
        'analysis, independent truth labels and a protected recorder before causal claims. '\n        'Paired p-value is exploratory and not adjusted for multiple testing.'
    )
    return out

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python taif-pilot-score.py attempts.csv')
    with open(sys.argv[1], newline='', encoding='utf-8') as f:
        print(json.dumps(score(csv.DictReader(f)), indent=2, sort_keys=True))
