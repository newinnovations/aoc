#!/usr/bin/env python3

DIRS = [-1, 0, 1]


def is_adjacent_ch(r, c):
    for dr in DIRS:
        for dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc] != "." and not grid[nr][nc].isdigit():
                    return True
    return False


def is_adjacent(r, c, number):
    return any(is_adjacent_ch(r, c + i) for i in range(len(number)))


with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

numbers = []
for r, row in enumerate(grid):
    number, start_c = "", -1
    for c, ch in enumerate(row):
        if ch.isdigit():
            if not number:
                start_c = c
            number += ch
        else:
            if number:
                numbers.append((r, start_c, number))
                number = ""
    if number:
        numbers.append((r, start_c, number))

print(sum(int(n) for r, c, n in numbers if is_adjacent(r, c, n)))  # 546312
