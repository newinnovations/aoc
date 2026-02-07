#!/usr/bin/env python3

from itertools import pairwise


def is_safe(report):
    delta_less_4 = all(abs(a - b) < 4 for a, b in pairwise(report))
    all_inc = all(a < b for a, b in pairwise(report))
    all_dec = all(a > b for a, b in pairwise(report))
    return delta_less_4 and (all_inc or all_dec)


num_safe = 0
with open(0) as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        if is_safe(report):
            num_safe += 1
        else:
            num_safe += any(
                is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
            )
print(num_safe)  # 665
