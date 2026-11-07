"""Conservative receipt-backed claim check. Synthetic only; protected key assumed.

Never trust claimant-supplied coverage labels or writer labels.
"""
from receipt_boundary import verify

KINDS = {'action_completed': ('action_succeeded', 'action_failed'),
         'alert_delivered': ('alert_delivered', 'alert_bounced')}

def decide_verified(claim, receipts, coverage_receipt, key, used_nonces=None):
    """Use caller-owned nonce registry; fail closed without one (not crash-durable)."""
    if claim.get('claim_type') not in KINDS:
        raise ValueError('unsupported claim')
    if not isinstance(used_nonces, set):
        return 'insufficient_evidence'
    try:
        expected = {k: claim[k] for k in ('scope_id', 'action_id', 'args_digest')}
    except KeyError:
        return 'insufficient_evidence'
    if not isinstance(receipts, (list, tuple)):
        return 'insufficient_evidence'
    if not isinstance(coverage_receipt, dict):
        return 'insufficient_evidence'
    cov_event, cov_sig = coverage_receipt.get('event'), coverage_receipt.get('signature')
    if not isinstance(cov_event, dict) or cov_event.get('kind') != 'coverage_complete':
        return 'insufficient_evidence'
    if not verify(cov_event, cov_sig, key, expected, used_nonces):
        return 'insufficient_evidence'
    good_kind, bad_kind = KINDS[claim['claim_type']]
    good = bad = False
    for receipt in receipts:
        if not isinstance(receipt, dict):
            continue
        event, sig = receipt.get('event'), receipt.get('signature')
        if not isinstance(event, dict) or event.get('kind') not in (good_kind, bad_kind):
            continue
        if verify(event, sig, key, expected, used_nonces):
            good |= event['kind'] == good_kind
            bad |= event['kind'] == bad_kind
    if good and bad:
        return 'insufficient_evidence'
    if bad:
        return 'refuted'
    if good:
        return 'supported'
    return 'insufficient_evidence'
