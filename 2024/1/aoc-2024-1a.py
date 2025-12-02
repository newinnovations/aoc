#!/usr/bin/env python3

import re

pattern = re.compile(r"(\d+)\s+(\d+)")
with open("input.txt") as f:
    pairs = [
        (int(a), int(b))
        for line in f
        if (m := pattern.match(line))
        for a, b in [m.groups()]
    ]
    list_a, list_b = map(sorted, zip(*pairs))

distance = 0
for a, b in zip(list_a, list_b):
    distance += abs(a - b)
print(distance)  # 1258579
