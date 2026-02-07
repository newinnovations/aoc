#!/usr/bin/env python3

import re

total = 0
with open(0) as f:
    orig, enabled, prog = f.read(), True, ""
    for i in range(len(orig)):
        if orig[i:].startswith("don't"):
            enabled = False
        elif orig[i:].startswith("do"):
            enabled = True
        if enabled:
            prog += orig[i]
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", prog):
        if len(a) < 4 and len(b) < 4:
            total += int(a) * int(b)
print(total)  # 189600467
