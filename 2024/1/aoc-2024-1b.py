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
    list_a, list_b = zip(*pairs)

similarity = 0
for a in list_a:
    similarity += sum([b for b in list_b if b == a])
print(similarity)  # 23981443
