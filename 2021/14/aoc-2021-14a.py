#!/usr/bin/env python3

from collections import defaultdict

with open(0) as f:
    template, rules = f.read().split("\n\n")
    rules = {r[:2]: r[6] for r in rules.splitlines()}

for _ in range(10):
    p = nt = template[0]
    for t in template[1:]:
        nt += rules[p + t] + t
        p = t
    template = nt

count = defaultdict(int)
for t in template:
    count[t] += 1

print(max(count.values()) - min(count.values()))  # 2587
