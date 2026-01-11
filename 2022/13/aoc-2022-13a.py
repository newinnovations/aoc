#!/usr/bin/env python3


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        return -1 if a < b else 1
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if c != 0:
                return c
        if len(a) < len(b):
            return -1
        if len(a) == len(b):
            return 0
        return 1
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])


total = 0
lines = []
with open(0) as f:
    for line in f:
        line = line.strip()
        if line:
            lines.append(eval(line.strip()))

input = [(lines[i], lines[i + 1]) for i in range(0, len(lines), 2)]
for i, (a, b) in enumerate(input):
    res = compare(a, b)
    if res == -1:
        total += i + 1

print(total)  # 5938
