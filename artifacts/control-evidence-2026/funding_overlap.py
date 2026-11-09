"""Fail-closed cross-funder budget reconciliation for Svyable grant proposals.

Input: JSON object with `allocations` records. Each record has `package`,
`date`, `contributor`, `deliverable`, `funder`, `hours`, and `amount_usd`.
Only funded/approved costs should be included in `allocations`.
This checks collisions, not sponsor permission, grant eligibility, or invoices.
"""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED = ('package', 'date', 'contributor', 'deliverable', 'funder')

def validate(document):
    if not isinstance(document, dict) or not isinstance(document.get('allocations'), list):
        raise ValueError('allocations must be a list')
    seen = {}
    errors = []
    totals = {}
    for i, a in enumerate(document['allocations']):
        if not isinstance(a, dict):
            errors.append(f'{i}: allocation must be object'); continue
        if any(not isinstance(a.get(k), str) or not a[k].strip() for k in REQUIRED):
            errors.append(f'{i}: missing required identity'); continue
        identity = tuple(a[k].strip().casefold() for k in REQUIRED[:4])
        funder = a['funder'].strip().casefold()
        if identity in seen:
            errors.append(f'{i}: duplicate work identity; prior allocation {seen[identity]} (same or different funder)')
        else:
            seen[identity] = i
        try:
            hours = Decimal(str(a['hours']))
            amount = Decimal(str(a['amount_usd']))
            if not hours.is_finite() or not amount.is_finite() or hours <= 0 or amount < 0:
                raise ValueError()
        except (KeyError, InvalidOperation, ValueError):
            errors.append(f'{i}: invalid hours/amount'); continue
        totals[funder] = totals.get(funder, Decimal(0)) + amount
    return {'ok': not errors, 'allocation_count': len(document['allocations']),
            'total_by_funder_usd': {k: str(v) for k,v in sorted(totals.items())}, 'errors': errors}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('json_file', type=Path)
    a = p.parse_args()
    result = validate(json.loads(a.json_file.read_text()))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['ok'] else 1)

if __name__ == '__main__': main()
