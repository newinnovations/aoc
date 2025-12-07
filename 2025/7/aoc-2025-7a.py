#!/usr/bin/env python3

with open("input.txt") as f:
    matrix = [list(line.strip()) for line in f]

num_split = 0
beams = [matrix[0].index("S")]
for row in matrix[1:]:
    for p in beams:
        if row[p] == "^":
            row[p - 1] = "|"
            row[p + 1] = "|"
            num_split += 1
        else:
            row[p] = "|"
    beams = [p for p in range(len(row)) if row[p] == "|"]
print(num_split)  # 1581
