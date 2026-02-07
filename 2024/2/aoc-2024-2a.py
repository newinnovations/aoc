#!/usr/bin/env python3

from itertools import pairwise

num_safe = 0
with open(0) as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        delta_less_4 = all(abs(a - b) < 4 for a, b in pairwise(report))
        all_inc = all(a < b for a, b in pairwise(report))
        all_dec = all(a > b for a, b in pairwise(report))
        num_safe += delta_less_4 and (all_inc or all_dec)
print(num_safe)  # 631
