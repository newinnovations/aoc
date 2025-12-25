#!/usr/bin/env python3

from itertools import pairwise

sequences = []
with open("input.txt") as f:
    for line in f:
        sequences.append(list(map(int, line.strip().split(" "))))


def calc_next(s):
    last = []
    d = s
    while True:
        last.append(d[-1])
        d = [b - a for a, b in pairwise(d)]
        if all(n == 0 for n in d):
            break
    return sum(last)


total = 0
for s in sequences:
    # print(s, end=": ")
    next = calc_next(s)
    # print(next)
    total += next
print(total)  # 1877825184
