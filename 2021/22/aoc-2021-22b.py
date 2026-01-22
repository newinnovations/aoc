#!/usr/bin/env python3

import re

p1 = re.compile(r"(-?\d+)")


commands, xm, ym, zm = [], set(), set(), set()
with open(0) as f:
    for line in f:
        state, coord = line.strip().split()
        xl, xh, yl, yh, zl, zh = map(int, p1.findall(coord))
        xh, yh, zh = xh + 1, yh + 1, zh + 1
        commands.append((state, xl, xh, yl, yh, zl, zh))
        xm.update([xl, xh])
        ym.update([yl, yh])
        zm.update([zl, zh])
xm, ym, zm = sorted(xm), sorted(ym), sorted(zm)

total = [
    [[False for _ in range(len(xm))] for _ in range(len(ym))] for _ in range(len(zm))
]
for state, xl, xh, yl, yh, zl, zh in commands:
    s = set()
    print(state, xl, xh, yl, yh, zl, zh)
    for x in range(xm.index(xl), xm.index(xh)):
        for y in range(ym.index(yl), ym.index(yh)):
            for z in range(zm.index(zl), zm.index(zh)):
                total[z][y][x] = state == "on"

total2 = 0
for x in range(len(xm)):
    for y in range(len(ym)):
        for z in range(len(zm)):
            if total[z][y][x]:
                total2 += (
                    (xm[x + 1] - xm[x]) * (ym[y + 1] - ym[y]) * (zm[z + 1] - zm[z])
                )
print(total2)  # 1201259791805392 (pypy 96 sec)
