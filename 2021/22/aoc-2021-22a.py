#!/usr/bin/env python3

import re

p1 = re.compile(r"(-?\d+)")


commands = []
with open(0) as f:
    for line in f:
        state, coord = line.strip().split()
        xl, xh, yl, yh, zl, zh = map(int, p1.findall(coord))
        xl, yl, zl = max(-50, xl), max(-50, yl), max(-50, zl)
        xh, yh, zh = 1 + min(50, xh), 1 + min(50, yh), 1 + min(50, zh)
        if xh > xl and yh > yl and zh > zl:
            commands.append((state, xl, xh, yl, yh, zl, zh))


total = set()
for state, xl, xh, yl, yh, zl, zh in commands:
    s = set()
    # print(state, xl, xh, yl, yh, zl, zh)
    for x in range(xl, xh):
        for y in range(yl, yh):
            for z in range(zl, zh):
                s.add((x, y, z))
    if state == "on":
        total |= s
    else:
        total -= s

print(len(total))  # 611176
