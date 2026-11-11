"""Synthetic local-only authorization fixture; NOT independent safety evidence."""
import hashlib
import json


def run_fixture(requests, allowed_actions=frozenset({'read_public'})):
    """Fail closed: exact allowlist; no real tools are executed."""
    trace = []
    for index, request in enumerate(requests):
        if not isinstance(request, dict) or not isinstance(request.get('action'), str):
            raise ValueError('each request needs a string action')
        action = request['action']
        permitted = action in allowed_actions
        trace.append({'index': index, 'action': action, 'decision': 'allow' if permitted else 'deny'})
    raw = json.dumps(trace, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    return {'trace': trace, 'sha256': hashlib.sha256(raw).hexdigest()}


if __name__ == '__main__':
    print(json.dumps(run_fixture([{'action': 'read_public'}, {'action': 'write_private'}, {'action': 'READ_PUBLIC'}]), sort_keys=True))
