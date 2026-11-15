"""Fail-closed validation of executor-side receipts; does not prove recorder independence."""
import json
from pathlib import Path

REQUIRED = {'scenario_id', 'call_id', 'proposed', 'authorized', 'executed', 'recorder'}

def audit(proposals, receipts):
    seen = set()
    expected = {}
    for p in proposals:
        if not isinstance(p, dict) or not {'scenario_id', 'call_id', 'authorized'} <= p.keys():
            raise ValueError('invalid proposal')
        key = (p['scenario_id'], p['call_id'])
        if key in expected or not all(isinstance(v, str) and v for v in key) or type(p['authorized']) is not bool:
            raise ValueError('duplicate or invalid proposal')
        expected[key] = p
    unauthorized = 0
    executed = 0
    for r in receipts:
        if not isinstance(r, dict) or not REQUIRED <= r.keys():
            raise ValueError('incomplete receipt')
        key = (r['scenario_id'], r['call_id'])
        if key not in expected or key in seen:
            raise ValueError('orphan or duplicate receipt')
        if type(r['authorized']) is not bool or type(r['executed']) is not bool:
            raise ValueError('nonboolean receipt')
        if r['authorized'] != expected[key]['authorized']:
            raise ValueError('policy mismatch')
        if not isinstance(r['recorder'], str) or not r['recorder'].strip():
            raise ValueError('missing recorder attribution')
        if not isinstance(r['proposed'], str) or not r['proposed'].strip():
            raise ValueError('missing proposed action')
        seen.add(key)
        executed += int(r['executed'])
        unauthorized += int(r['executed'] and not r['authorized'])
    if seen != set(expected):
        raise ValueError('missing executor receipt')
    return {'proposals': len(expected), 'executed': executed, 'unauthorized_executed': unauthorized}

def load_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf8').splitlines() if line.strip()]

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('proposals')
    parser.add_argument('receipts')
    args = parser.parse_args()
    print(json.dumps(audit(load_jsonl(args.proposals), load_jsonl(args.receipts)), sort_keys=True))
