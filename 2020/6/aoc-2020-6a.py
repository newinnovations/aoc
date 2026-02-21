#!/usr/bin/env python3

with open(0) as f:
    groups = f.read().split("\n\n")
    groups = [g.split() for g in groups]

total = 0
for group in groups:
    s = set()
    for a in group:
        s.update(a)
    total += len(s)

print(total)  # 6551
