"""Fail-closed preflight for proposed cross-funder work allocations.

This is a planning control, not proof of incurred expenses or sponsor consent.
Each scope_id must identify a unique deliverable across all funding requests,
regardless of dates, contributors, or alternative descriptions.
"""
from decimal import Decimal, InvalidOperation


def check_release(allocations, expected_funders=('bluedot', 'ea')):
    errors = []
    if not isinstance(allocations, list) or not allocations:
        return {'ok': False, 'errors': ['nonempty allocation schedule required']}
    seen = {}
    funders = set()
    for i, a in enumerate(allocations):
        if not isinstance(a, dict):
            errors.append(f'{i}: record must be object')
            continue
        scope = a.get('scope_id')
        funder = a.get('funder')
        if not isinstance(scope, str) or not scope.strip() or not isinstance(funder, str) or not funder.strip():
            errors.append(f'{i}: scope_id and funder required')
            continue
        scope, funder = scope.strip().casefold(), funder.strip().casefold()
        if scope in seen:
            errors.append(f'{i}: scope_id {scope} already allocated at {seen[scope]}')
        else:
            seen[scope] = i
        funders.add(funder)
        try:
            hours = Decimal(str(a['hours']))
            amount = Decimal(str(a['amount_usd']))
            if not hours.is_finite() or not amount.is_finite() or hours <= 0 or amount < 0:
                raise ValueError
        except (KeyError, ValueError, InvalidOperation):
            errors.append(f'{i}: invalid hours or amount')
    allowed = {x.casefold() for x in expected_funders}
    if funders - allowed:
        errors.append('unrecognized funder(s): ' + ', '.join(sorted(funders - allowed)))
    return {'ok': not errors, 'errors': errors}
