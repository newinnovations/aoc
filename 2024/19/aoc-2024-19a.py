#!/usr/bin/env python3

from functools import cache

available, required = [], []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if "," in line:
            available = line.split(", ")
        elif line:
            required.append(line)


@cache
def is_possible(pattern):
    if not pattern:
        return True
    return any(
        is_possible(pattern[len(a) :]) for a in available if pattern.startswith(a)
    )


print(sum(is_possible(pattern) for pattern in required))
