#!/usr/bin/env python3
"""Synthetic HMAC receipt boundary. Assumes claimant cannot access recorder key.
This fixture does NOT establish independent deployment provenance or coverage.
"""
import hashlib
import hmac
import json
import unittest

FIELDS = ("scope_id", "action_id", "args_digest", "kind", "nonce")

def canonical(event):
    if not isinstance(event, dict) or any(not isinstance(event.get(k), str) or not event[k] for k in FIELDS):
        raise ValueError("invalid receipt")
    return json.dumps({k: event[k] for k in FIELDS}, sort_keys=True, separators=(",", ":")).encode()

def sign(event, key):
    return hmac.new(key, canonical(event), hashlib.sha256).hexdigest()

def verify(event, signature, key, expected, used_nonces):
    try:
        raw = canonical(event)
        if not isinstance(signature, str) or len(signature) != 64:
            return False
        if any(event[k] != expected[k] for k in ("scope_id", "action_id", "args_digest")):
            return False
        if event["nonce"] in used_nonces:
            return False
        if not hmac.compare_digest(hmac.new(key, raw, hashlib.sha256).hexdigest(), signature):
            return False
    except (KeyError, TypeError, ValueError):
        return False
    used_nonces.add(event["nonce"])
    return True

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.key = b"fixture-only-recorder-key"
        self.event = dict(scope_id="sandbox", action_id="write-1", args_digest="sha256:abc", kind="action_succeeded", nonce="n-1")
        self.expected = {k: self.event[k] for k in ("scope_id", "action_id", "args_digest")}
        self.sig = sign(self.event, self.key)

    def test_valid_receipt(self):
        self.assertTrue(verify(self.event, self.sig, self.key, self.expected, set()))

    def test_wrong_key(self):
        self.assertFalse(verify(self.event, self.sig, b"wrong", self.expected, set()))

    def test_tampered_arguments(self):
        self.assertFalse(verify(dict(self.event, args_digest="sha256:other"), self.sig, self.key, self.expected, set()))

    def test_tampered_kind(self):
        self.assertFalse(verify(dict(self.event, kind="action_failed"), self.sig, self.key, self.expected, set()))

    def test_replay(self):
        used = set()
        self.assertTrue(verify(self.event, self.sig, self.key, self.expected, used))
        self.assertFalse(verify(self.event, self.sig, self.key, self.expected, used))

    def test_missing_signature(self):
        self.assertFalse(verify(self.event, None, self.key, self.expected, set()))

    def test_writer_label_spoof(self):
        self.assertFalse(verify(dict(self.event, writer="independent", nonce="new-nonce"), self.sig, self.key, self.expected, set()))

    def test_wrong_scope(self):
        event = dict(self.event, scope_id="other")
        self.assertFalse(verify(event, sign(event, self.key), self.key, self.expected, set()))

    def test_invalid_fields(self):
        self.assertFalse(verify(dict(self.event, nonce=""), self.sig, self.key, self.expected, set()))

if __name__ == "__main__":
    unittest.main(verbosity=2)
