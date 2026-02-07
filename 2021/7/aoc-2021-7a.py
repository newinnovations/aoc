#!/usr/bin/env python3

total = 0
with open(0) as f:
    pos = list(map(int, f.read().split(",")))
pos.sort()

n = pos[len(pos) // 2]

print(sum(abs(n - i) for i in pos))  # 352707
