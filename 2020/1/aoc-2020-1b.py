#!/usr/bin/env python3

from itertools import combinations

with open(0) as f:
    entries = list(map(int, (line for line in f.read().splitlines())))

for a, b, c in combinations(entries, 3):
    if a + b + c == 2020:
        print(a * b * c)  # 165795564
