#!/usr/bin/env python3

import re

pos, password, pattern = 50, 0, re.compile(r"([LR])(\d+)")
with open("input.txt") as f:
    for line in f:
        if match := pattern.match(line):
            dir, count = match.groups()
            pos = (pos + int(count) if dir == "R" else pos - int(count)) % 100
            password += pos == 0
print(password)  # 982
