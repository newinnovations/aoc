#!/usr/bin/env python3

import re


def calc(t, v):
    return v * t - t * (t - 1) // 2


def calc_x(t, vx):
    return calc(min(t, vx), vx)


xl, xh, yl, yh = map(int, re.findall(r"-?\d+", open(0).read()))
print(xl, xh, yl, yh)

# * time and X velocity does not matter if there is a X velocity
#   where X does not increase anymore with the x range, which
#   applies here both with the sample and puzzle data.
# * to maximize y means to maximize vy
# * y always touches zero when coming down
# * first stop after zero is `-vy - 1`
# * largest vy is the one where the first stop after zero is still
#   within the target: -vy - 1 == yl
# * highest position of y is always reached at `t == vy`

vy = -(yl + 1)
print(calc(vy, vy))  # 9730
