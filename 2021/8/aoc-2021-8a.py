#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        input, output = line.split(" | ")
        for d in output.split():
            if len(d) in [2, 3, 4, 7]:
                total += 1
print(total)  # 456
