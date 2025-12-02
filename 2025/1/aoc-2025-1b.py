#!/usr/bin/env python3

import re

pos, password, pattern = 50, 0, re.compile(r"([LR])(\d+)")
with open("input.txt") as f:
    for line in f:
        if match := pattern.match(line):
            dir, count = match.groups()
            delta = 1 if dir == "R" else -1
            for _ in range(int(count)):
                pos = (pos + delta) % 100
                password += pos == 0
print(password)  # 6106
