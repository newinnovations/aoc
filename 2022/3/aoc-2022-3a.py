#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        a, b = line[: len(line) // 2], line[len(line) // 2 :]
        both = (set(a) & set(b)).pop()
        prio = 1 + ord(both) - ord("a") if both >= "a" else 27 + ord(both) - ord("A")
        total += prio
print(total)  # 7824
