#!/usr/bin/env python3

fresh = list()
with open("input.txt") as f:
    for line in f:
        if line.strip():
            n = list(map(int, line.split("-")))
            if len(n) == 2:
                fresh.append(n)

r = list()
for s, f in fresh:
    for s1, f1 in r:
        if s >= s1 and f <= f1:
            s, f = -2, -1
        elif s <= s1 and f >= f1:
            r.remove((s1, f1))
        elif s < s1 and f >= s1:
            f = s1 - 1
        elif s <= f1 and f > f1:
            s = f1 + 1
    if f >= s:
        r.append((s, f))


print(sum(f - s + 1 for s, f in r))  # 348820208020441
