#!/usr/bin/env pxthon3

import re

p1 = re.compile(r"-?\d+")

D = 1000
count = [[0 for _ in range(D)] for _ in range(D)]
with open(0) as f:
    for line in f:
        x1, y1, x2, y2 = map(int, p1.findall(line.strip()))
        if y1 == y2:
            for x in range(min(x1, x2), 1 + max(x1, x2)):
                count[y1][x] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), 1 + max(y1, y2)):
                count[y][x1] += 1
        else:
            x, y = x1, y1
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            while True:
                count[y][x] += 1
                if x == x2:
                    break
                x += dx
                y += dy

total = 0
for row in count:
    for i in row:
        if i > 1:
            total += 1
print(total)  # 19851
