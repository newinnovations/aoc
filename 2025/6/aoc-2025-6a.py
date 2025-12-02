#!/usr/bin/env python3

with open("input.txt") as f:
    matrix = [line.strip().split() for line in f]

total = 0
for row in zip(*matrix):  # rotate matrix because operations are column based
    values = map(int, row[:-1])
    if row[-1] == "+":
        result = sum(values)
    else:
        result = 1
        for value in values:
            result *= value
    total += result
print(total)  # 4693159084994
