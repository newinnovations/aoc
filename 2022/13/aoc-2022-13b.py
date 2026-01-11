#!/usr/bin/env python3

from functools import cmp_to_key


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


input = [eval(line) for line in open(0) if line.strip()]
D2, D6 = [[2]], [[6]]
input += [D2, D6]
input.sort(key=cmp_to_key(compare))
print((input.index(D2) + 1) * (input.index(D6) + 1))  # 29025
