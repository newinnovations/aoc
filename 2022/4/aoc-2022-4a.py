#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        f1, t1, f2, t2 = map(
            int, line.strip().replace("-", " ").replace(",", " ").split()
        )
        inside = (f1 >= f2 and t1 <= t2) or (f2 >= f1 and t2 <= t1)
        if inside:
            total += 1

print(total)  # 498
