#!/usr/bin/env python3

from collections import defaultdict
from itertools import combinations

connections = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        pc = line.strip().split("-")
        connections[pc[0]].add(pc[1])
        connections[pc[1]].add(pc[0])

groups = set()
for pc, connected_pcs in connections.items():
    if pc[0] == "t":
        for a, b in combinations(connected_pcs, 2):
            if b in connections[a]:
                groups.add(tuple(sorted([pc, a, b])))

print(len(groups))  # 998
