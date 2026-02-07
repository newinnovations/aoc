#!/usr/bin/env python3

with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]

e = g = 0
for row in zip(*grid):
    ones = sum(row)
    zeros = len(row) - ones
    g = g * 2 + int(ones > zeros)
    e = e * 2 + int(ones < zeros)

print(e * g)  # 841526
