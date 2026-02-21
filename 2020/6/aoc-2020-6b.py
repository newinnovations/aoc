#!/usr/bin/env python3

with open(0) as f:
    groups = f.read().split("\n\n")
    groups = [g.split() for g in groups]

total = 0
for group in groups:
    s = set(group[0])
    for a in group[1:]:
        s.intersection_update(a)
    total += len(s)

print(total)  # 3358
