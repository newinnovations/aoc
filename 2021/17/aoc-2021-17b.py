#!/usr/bin/env python3

import re
from math import ceil, floor, sqrt


def calc(t, v):
    return v * t - t * (t - 1) // 2


def calc_x(t, vx):
    return calc(min(t, vx), vx)


def solve_t(x, v):
    """
    Solve x = v*t - t*(t - 1)/2 for t.

    Reduces to: t^2 - (2v + 1)*t + 2x = 0
    Discriminant: Δ = (2v + 1)^2 - 8x
    Root 1: (2v + 1 - sqrt(Δ)) / 2 (not relevant: negative)
    Root 2: (2v + 1 + sqrt(Δ)) / 2
    """
    disc = (2 * v + 1) ** 2 - 8 * x
    if disc < 0:
        raise ValueError(f"No real solution: discriminant Δ={disc} < 0")
    # Roots: (2v + 1 ± sqrt(Δ))/2
    return (2.0 * v + 1.0 + sqrt(disc)) / 2.0


xl, xh, yl, yh = map(int, re.findall(r"-?\d+", open(0).read()))
print(xl, xh, yl, yh)

s = set()
for vy in range(yl, -yl):
    t1 = floor(solve_t(yh, vy))
    t2 = ceil(solve_t(yl, vy))
    for t in range(t1, t2 + 1):
        y = calc(t, vy)
        if yl <= y <= yh:
            for vx in range(xh + 1):
                x = calc_x(t, vx)
                if xl <= x <= xh:
                    s.add((vx, vy))
print(len(s))  # 4110
