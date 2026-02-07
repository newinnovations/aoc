#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        d = [int(c) for c in line.strip() if c.isdigit()]
        total += d[0] * 10 + d[-1]
print(total)  # 54605
