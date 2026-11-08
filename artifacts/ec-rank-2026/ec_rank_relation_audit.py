#!/usr/bin/env python3
"""Exact rational group-law audit of unranked integral EC candidates.

An explicit P+Q=R relation disproves independence of the FULL supplied
point list. Absence of short relations does NOT certify independence.
"""
from fractions import Fraction
import json


def negate(p):
    return None if p is None else (p[0], -p[1])


def on_curve(p, a, b):
    if p is None:
        return True
    x, y = p
    return y*y == x*x*x + a*x + b


def add(p, q, a):
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u and y == -v:
        return None
    if p == q:
        if y == 0:
            return None
        slope = (3*x*x+a)/(2*y)
    else:
        slope = (v-y)/(u-x)
    X = slope*slope-x-u
    return (X, slope*(x-X)-y)


def relation_audit(a, b, points):
    """Find distinct-pair and doubling relations among input points and signs."""
    if 4*a*a*a+27*b*b == 0:
        raise ValueError('singular curve')
    pts = [(Fraction(x), Fraction(y)) for x,y in points]
    if any(not on_curve(p,a,b) for p in pts):
        raise ValueError('off-curve point')
    if len(set(pts)) != len(pts):
        raise ValueError('repeated point')
    lookup = {p:i for i,p in enumerate(pts)}
    found=[]
    for i in range(len(pts)):
        for j in range(i,len(pts)):
            r=add(pts[i],pts[j],a)
            for sign, target in ((1,r),(-1,negate(r))):
                if target is not None and target in lookup:
                    k=lookup[target]
                    found.append({'i':i,'j':j,'k':k,'sign':sign})
    return found


def main():
    from ec_rank_probe import search
    candidates=search(30,60,20,6,5)
    out=[]
    for c in candidates:
        a,b=c['a_invariants'][-2:]
        relations=relation_audit(a,b,c['integral_point_representatives'])
        out.append({'a_invariants':c['a_invariants'],
                    'point_representatives':c['point_count'],
                    'short_relations':len(relations),
                    'first_relation':relations[0] if relations else None,
                    'independence_certified':False})
    print(json.dumps({'purpose':'negative independence audit only; no certified rank or official score',
                      'results':out},indent=2))


if __name__=='__main__':
    main()
