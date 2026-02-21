#!/usr/bin/env python3

from itertools import combinations

with open(0) as f:
    entries = list(map(int, (line for line in f.read().splitlines())))

for a, b in combinations(entries, 2):
    if a + b == 2020:
        print(a * b)  # 241861950
