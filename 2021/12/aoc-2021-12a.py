#!/usr/bin/env python3

from collections import defaultdict

conn = defaultdict(set)
with open(0) as f:
    for line in f:
        t, f = line.strip().split("-")
        conn[t].add(f)
        conn[f].add(t)


def is_small(node):
    return node[0] == node[0].lower()


def count(current, seen):
    if current == "end":
        return 1
    total = 0
    for n in conn[current]:
        if is_small(n):
            if n in seen:
                continue
            else:
                total += count(n, seen.union([n]))
        else:
            total += count(n, seen)
    return total


print(count("start", frozenset(["start"])))  # 5178
