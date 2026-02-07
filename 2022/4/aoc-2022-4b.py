#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        f1, t1, f2, t2 = map(
            int, line.strip().replace("-", " ").replace(",", " ").split()
        )
        overlap = (f1 <= f2 <= t1) or (f2 <= f1 <= t2)
        if overlap:
            total += 1

print(total)  # 859
