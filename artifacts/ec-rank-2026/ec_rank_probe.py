#!/usr/bin/env python3
"""Reproducible, UNRANKED search for integral-point-rich elliptic curves.

This is an original candidate generator for Layr-Labs elliptic-rank challenge,
NOT a rank certificate, novelty check, or official benchmark score.
Only publish candidates after checking the competition's complete rules.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from math import isqrt, log


def integral_points(a: int, b: int, xmin: int, xmax: int):
    """Find positive-y integral witnesses; y=0 is rational 2-torsion, not rank evidence."""
    out = []
    for x in range(xmin, xmax + 1):
        rhs = x*x*x + a*x + b
        if rhs > 0:
            y = isqrt(rhs)
            if y*y == rhs:
                out.append((x, y))
    return out


def nonsingular(a: int, b: int) -> bool:
    return 4*a*a*a + 27*b*b != 0


def naive_height(a: int, b: int) -> float:
    c4, c6 = -48*a, -864*b
    return log(max(abs(c4)**3, c6*c6, 1)) / 12


def search(amax: int = 30, bmax: int = 60, xmax: int = 20,
           min_points: int = 5, limit: int = 10):
    if min(amax,bmax,xmax,limit) < 1 or min_points < 0:
        raise ValueError('bounds/limit must be positive; min_points nonnegative')
    candidates = []
    for a in range(-amax, amax + 1):
        for b in range(-bmax, bmax + 1):
            if not nonsingular(a,b):
                continue
            points = integral_points(a,b,-xmax,xmax)
            if len(points) >= min_points:
                candidates.append({'a_invariants':[0,0,0,a,b],
                                   'integral_point_representatives':points,
                                   'point_count':len(points),
                                   'naive_height':round(naive_height(a,b),8)})
    candidates.sort(key=lambda c:(-c['point_count'],c['naive_height'],c['a_invariants']))
    return candidates[:limit]


def build_report(amax=30,bmax=60,xmax=20,min_points=5,limit=10):
    options={'amax':amax,'bmax':bmax,'xmax':xmax,'min_points':min_points,'limit':limit}
    candidates=search(**options)
    body={'purpose':'unranked original candidate discovery; NOT a certified rank or prize result',
          'official_verification_required':['PARI/GP 2.17.4 minimal model','known/isogeny/twist novelty gate',
               'torsion stripping','canonical height-pairing independence','nonregression','official ranked evaluator'],
          'bounds':options,'candidates':candidates}
    body['experiment_sha256']=hashlib.sha256(json.dumps({'bounds':options,'candidates':candidates},sort_keys=True).encode()).hexdigest()
    return body


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name,default in [('amax',30),('bmax',60),('xmax',20),('min-points',5),('limit',10)]:
        p.add_argument('--'+name,type=int,default=default)
    a=p.parse_args()
    print(json.dumps(build_report(a.amax,a.bmax,a.xmax,a.min_points,a.limit),indent=2))

if __name__=='__main__':
    main()
