#!/usr/bin/env python3

from itertools import combinations

with open(0) as f:
    xmas = list(map(int, (line for line in f.read().splitlines())))

PREAMBLE = 5 if len(xmas) < 100 else 25

invalid_number = 1
for n, x in enumerate(xmas[PREAMBLE:]):
    sums = set(a + b for a, b in combinations(xmas[n : n + PREAMBLE], 2))
    if x not in sums:
        invalid_number = x
        break

print(invalid_number)  # 675280050
