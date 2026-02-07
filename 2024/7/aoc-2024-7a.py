#!/usr/bin/env python3
import re


def solvable(total, parts):
    res = (len(parts) == 1 and total == parts[0]) or (
        len(parts) > 1
        and (
            solvable(total, [parts[0] + parts[1]] + parts[2:])
            or solvable(total, [parts[0] * parts[1]] + parts[2:])
        )
    )
    return res


total = 0
with open(0) as f:
    for line in f:
        n = list(map(int, re.split(r": | ", line)))
        result, parts = n[0], n[1:]
        if solvable(result, parts):
            total += result
print(total)  # 1545311493300
