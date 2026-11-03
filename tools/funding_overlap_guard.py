"""Validate proposed future grant work allocations. No third-party data access."""
import csv
import datetime as dt
import decimal
import sys
from collections import defaultdict

FIELDS = ('task_id','funder','person','date','start_minute','end_minute','hours','rate','deliverable_id','evidence_link','approval')
D = decimal.Decimal

def validate(rows):
    errors = []
    seen = defaultdict(list)
    deliverables = defaultdict(set)
    for i, row in enumerate(rows, 2):
        missing = [k for k in FIELDS if not str(row.get(k, '')).strip()]
        if missing:
            errors.append(f'row {i}: missing {",".join(missing)}')
            continue
        try:
            dt.date.fromisoformat(row['date'])
            start, end = int(row['start_minute']), int(row['end_minute'])
            hours, rate = D(row['hours']), D(row['rate'])
            if not (0 <= start < end <= 1440): raise ValueError('invalid time interval')
            if hours <= 0 or rate < 0 or hours != D(end-start)/D(60): raise ValueError('hours/rate/interval mismatch')
            if not hours.is_finite() or not rate.is_finite(): raise ValueError('nonfinite number')
        except (ValueError, decimal.InvalidOperation) as e:
            errors.append(f'row {i}: invalid date/time/cost: {e}')
            continue
        key = (row['person'].strip().casefold(), row['date'])
        for prior_start, prior_end, prior_funder, prior_i in seen[key]:
            if start < prior_end and prior_start < end:
                errors.append(f'row {i}: overlapping person-time with row {prior_i} ({prior_funder})')
        seen[key].append((start,end,row['funder'],i))
        deliverables[row['deliverable_id']].add(row['funder'])
        if row['approval'].strip().lower() != 'approved':
            errors.append(f'row {i}: applicant approval not recorded')
    for identifier, funders in deliverables.items():
        if len(funders) > 1:
            errors.append(f'deliverable {identifier}: charged to multiple funders')
    return errors

def main(path):
    with open(path, newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or set(FIELDS) - set(reader.fieldnames):
            print('FAIL: missing required CSV headers'); return 2
        errors = validate(list(reader))
    for e in errors: print('FAIL:', e)
    if errors: return 1
    print('PASS: no listed collisions; source accuracy, consent, eligibility and sponsor approval NOT verified')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]) if len(sys.argv) == 2 else 2)
