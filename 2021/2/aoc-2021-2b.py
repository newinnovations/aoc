#!/usr/bin/env python3

x = y = aim = 0
with open(0) as f:
    for line in f:
        dir, amount = line.strip().split()
        if dir == "up":
            aim -= int(amount)
        if dir == "down":
            aim += int(amount)
        if dir == "forward":
            x += int(amount)
            y += aim * int(amount)

print(x * y)  # 1872757425
