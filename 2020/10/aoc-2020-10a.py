#!/usr/bin/env python3

from itertools import pairwise

with open(0) as f:
    joltage = list(map(int, (line for line in f.read().splitlines())))

joltage.sort()
joltage.insert(0, 0)
joltage.append(joltage[-1] + 3)

diffs = [b - a for a, b in pairwise(joltage)]

ones = sum(d == 1 for d in diffs)
threes = sum(d == 3 for d in diffs)

print(ones * threes)  # 1984
