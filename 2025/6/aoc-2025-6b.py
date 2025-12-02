#!/usr/bin/env python3

from itertools import pairwise

with open("input.txt") as f:
    lines = [line.rstrip("\r\n") for line in f]

# operator positions on last line mark start of column
op_pos = [pos for pos, char in enumerate(lines[-1]) if char != " "]
op_pos.append(len(lines[-1]) + 1)  # fake operator location to mark end of last column
matrix = [[line[s : f - 1] for s, f in pairwise(op_pos)] for line in lines]

total = 0
for row in zip(*matrix):  # rotate matrix because operations are column based
    values = [list(a) for a in row[:-1]]  # split strings in chars
    # recreate as integers after rotation
    values = [int("".join(a).strip()) for a in zip(*values)]
    if row[-1][0] == "+":
        result = sum(values)
    else:
        result = 1
        for value in values:
            result *= value
    total += result
print(total)  # 11643736116335
