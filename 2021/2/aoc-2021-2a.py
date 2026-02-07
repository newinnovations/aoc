#!/usr/bin/env python3

x = y = 0
with open(0) as f:
    for line in f:
        dir, amount = line.strip().split()
        if dir == "up":
            y -= int(amount)
        if dir == "down":
            y += int(amount)
        if dir == "forward":
            x += int(amount)

print(x * y)  # 1636725
