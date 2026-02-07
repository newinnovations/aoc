#!/usr/bin/env python3

from itertools import pairwise

with open(0) as f:
    n = list(map(int, f.read().split()))

total = 0
for a, b in pairwise(sum(n[i : i + 3]) for i in range(len(n) - 2)):
    total += int(b > a)
print(total)  # 1346
