#!/usr/bin/env python3

prod, fresh = list(), list()
with open("input.txt") as f:
    for line in f:
        if line.strip():
            n = list(map(int, line.split("-")))
            if len(n) == 1:
                prod.append(n[0])
            elif len(n) == 2:
                fresh.append(n)

print(sum(any(p >= s and p <= f for s, f in fresh) for p in prod))  # 681
