#!/usr/bin/env python3

from itertools import batched

total = 0
lines = []
with open(0) as f:
    for line in f:
        lines.append(line.strip())

for group in batched(lines, 3):
    common = set(group[0])
    for g in group[1:]:
        common &= set(g)
    common = common.pop()
    prio = 1 + ord(common) - ord("a") if common >= "a" else 27 + ord(common) - ord("A")
    total += prio

print(total)  # 2798
