#!/usr/bin/env python3

with open(0) as f:
    total = 0
    for line in f:
        line = line.strip().split()
        p = line.index("|")
        winning = list(map(int, line[2:p]))
        have = list(map(int, line[p + 1 :]))
        worth = 0
        for h in have:
            if h in winning:
                if not worth:
                    worth = 1
                else:
                    worth *= 2
        total += worth
    print(total)  # 25174
