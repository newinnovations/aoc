#!/usr/bin/env python3

from itertools import pairwise

sequences = []
with open("input.txt") as f:
    for line in f:
        sequences.append(list(map(int, line.strip().split(" "))))


def calc_previous(s):
    first = []
    d = s
    while True:
        first.append(d[0])
        d = [b - a for a, b in pairwise(d)]
        if all(n == 0 for n in d):
            break
    return sum(-x if i % 2 else x for i, x in enumerate(first))


total = 0
for s in sequences:
    previous = calc_previous(s)
    # print(previous, s)
    total += previous
print(total)  # 1108
