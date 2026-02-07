#!/usr/bin/env python3

OP = "ABC"
YOU = "XYZ"

total = 0
with open(0) as f:
    for line in f:
        opponent, you = line.strip().split()
        op = OP.index(opponent)
        you = YOU.index(you)
        win = (you == 2 and op == 1) or (you == 1 and op == 0) or (you == 0 and op == 2)
        total += 1 + you
        if win:
            total += 6
        if op == you:
            total += 3
print(total)  # 10310
