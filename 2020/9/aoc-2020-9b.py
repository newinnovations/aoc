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

for start in range(len(xmas) - 1):
    for end in range(start + 2, 1 + len(xmas)):
        s = sum(xmas[start:end])
        if s == invalid_number:
            print(min(xmas[start:end]) + max(xmas[start:end]))  # 96081673
            break
        if s > invalid_number:
            break
