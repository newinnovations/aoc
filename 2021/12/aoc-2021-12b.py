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


def count(current, seen_once, seen_twice):
    if current == "end":
        return 1
    total = 0
    for n in conn[current]:
        if n == "start":
            continue
        if is_small(n):
            if n in seen_once:
                if seen_twice:
                    continue
                total += count(n, seen_once, seen_twice.union([n]))
            else:
                total += count(n, seen_once.union([n]), seen_twice)
        else:
            total += count(n, seen_once, seen_twice)
    return total


print(count("start", frozenset(["start"]), frozenset()))  # 130094
