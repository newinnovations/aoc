#!/usr/bin/env python3

from itertools import groupby, pairwise

with open(0) as f:
    joltage = list(map(int, (line for line in f.read().splitlines())))

joltage.sort()
joltage.insert(0, 0)
joltage.append(joltage[-1] + 3)

diffs = [b - a for a, b in pairwise(joltage)]

one_groups = [len(list(group)) for key, group in groupby(diffs) if key == 1]

# 1 -> 1: 20 23 24 27
# 2 -> 2: 20 23 24 25 28
#         20 23 25 28
# 3 -> 4: 20 23 24 25 26 29
#         20 23 25 26 29
#         20 23 24 26 29
#         20 23 26 29
# 4 -> 7: 20 23 24 25 26 27 30
#         20 23 25 26 27 30
#         20 23 24 26 27 30
#         20 23 24 25 27 30
#         20 23 26 27 30
#         20 23 24 27 30
#         20 23 25 27 30
# **NOT** 20 23 27 30

MULT = {1: 1, 2: 2, 3: 4, 4: 7}

total = 1
for o in one_groups:
    total *= MULT[o]
print(total)  # 3543369523456
