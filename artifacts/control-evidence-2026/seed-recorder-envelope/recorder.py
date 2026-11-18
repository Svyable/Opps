"""Minimal authenticated observation envelope; NOT an independent executor.

The caller must protect the secret outside the untrusted agent boundary. This
module authenticates records, not physical side effects or recorder isolation.
"""
import hashlib
import hmac
import json


def canonical(event):
    return json.dumps(event, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def sign(event, key):
    return hmac.new(key, canonical(event), hashlib.sha256).hexdigest()


def verify(event, tag, key, expected_run, expected_action, expected_digest):
    required = {'run_id', 'action_id', 'path', 'sha256', 'observed'}
    if set(event) != required or not isinstance(tag, str):
        return 'UNKNOWN'
    if event['run_id'] != expected_run or event['action_id'] != expected_action:
        return 'REJECT'
    if not hmac.compare_digest(sign(event, key), tag):
        return 'REJECT'
    if event['observed'] is not True:
        return 'UNKNOWN'
    if event['sha256'] != expected_digest:
        return 'REJECT'
    return 'VERIFIED'
