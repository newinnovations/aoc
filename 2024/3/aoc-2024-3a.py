#!/usr/bin/env python3

import re

total = 0
with open(0) as f:
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", f.read()):
        if len(a) < 4 and len(b) < 4:
            total += int(a) * int(b)
print(total)  # 189600467
