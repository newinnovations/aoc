#!/usr/bin/env python3

with open(0) as f:
    area = [list(map(int, list(line.strip()))) for line in f]

visible = set()
for r, row in enumerate(area):
    for c, n in enumerate(row):
        if max([-1] + row[:c]) < n:
            visible.add((r, c))
        if max([-1] + row[c + 1 :]) < n:
            visible.add((r, c))

for r, row in enumerate(zip(*area)):
    row = list(row)
    for c, n in enumerate(row):
        if max([-1] + row[:c]) < n:
            visible.add((c, r))
        if max([-1] + row[c + 1 :]) < n:
            visible.add((c, r))

print(len(visible))  # 1870
