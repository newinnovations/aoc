#!/usr/bin/env python3

from functools import cache

with open(0) as f:
    template, rules = f.read().split("\n\n")
    rules = {r[:2]: r[6] for r in rules.splitlines()}
elements = sorted(set("".join(rules.keys())))
indx = {e: i for i, e in enumerate(elements)}


@cache
def num(pair1, pair2, level):
    if level == 0:
        c1 = [int(ch == pair1) for ch in elements]
        c2 = [int(ch == pair2) for ch in elements]
        return [a + b for a, b in zip(c1, c2)]
    else:
        r = rules[pair1 + pair2]
        c1 = num(pair1, r, level - 1)
        c2 = num(r, pair2, level - 1)
        t = [a + b for a, b in zip(c1, c2)]
        t[indx[r]] -= 1
        return t


N = 40
total = [0 for _ in elements]
for i, a in enumerate(template[:-1]):
    b = template[i + 1]
    p = num(a, b, N)
    total = [a + b for a, b in zip(total, p)]
    if i > 0:
        total[indx[a]] -= 1
print(max(total) - min(total))  # 3318837563123
