#!/usr/bin/env python3

total = 0
elves = open(0).read().split("\n\n")
for e in elves:
    total = max(total, sum(map(int, e.split())))
print(total)  # 68775
