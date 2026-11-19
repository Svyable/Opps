"""Bounded pre/post-state gate for disposable local file writes.

Not a security boundary against a malicious same-host process. In particular,
this does not establish process identity or protect the observer's key.
"""
import hashlib
from pathlib import Path
import secrets
import tempfile


def run_fresh_trial(payload=b'authorized harmless write', *, prepopulate=False,
                    omit_executor=False, tamper=False):
    """Return VERIFIED/REJECT/UNKNOWN with an observer-owned fresh target.

    A preexisting target is always REJECT, even if its digest matches payload.
    The nonce is generated per trial and is not chosen by the executor.
    """
    with tempfile.TemporaryDirectory(prefix='observer-owned-') as root:
        target = Path(root) / (secrets.token_hex(16) + '.bin')
        if prepopulate:
            target.write_bytes(payload)
        if target.exists():
            return 'REJECT'
        before = target.exists()
        if not omit_executor:
            target.write_bytes(payload)
        if tamper and target.exists():
            target.write_bytes(b'substituted')
        if not target.exists():
            return 'UNKNOWN'
        observed = hashlib.sha256(target.read_bytes()).digest()
        expected = hashlib.sha256(payload).digest()
        return 'VERIFIED' if not before and observed == expected else 'REJECT'
