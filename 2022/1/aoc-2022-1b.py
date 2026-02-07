#!/usr/bin/env python3

totals = []
elves = open(0).read().split("\n\n")
for e in elves:
    totals.append(sum(map(int, e.split())))
totals.sort()
print(sum(totals[-3:]))  # 202585
