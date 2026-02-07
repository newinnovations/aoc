#!/usr/bin/env python3

OP = "ABC"
YOU = "XYZ"

total = 0
with open(0) as f:
    for line in f:
        opponent, outcome = line.strip().split()
        op = OP.index(opponent)
        if outcome == "X":  # loose
            you = op - 1
            if you == -1:
                you = 2
        elif outcome == "Z":  # win
            total += 6
            you = op + 1
            if you == 3:
                you = 0
        else:
            total += 3
            you = op
        total += 1 + you
print(total)  # 14859
