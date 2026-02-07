#!/usr/bin/env python3

DIRS = [-1, 0, 1]


def is_adjacent_number(r, c, idx):
    nr, nc, number = numbers[idx]
    return nr - 1 <= r <= nr + 1 and nc - 1 <= c <= nc + len(number)


def get_adjacent_numbers(r, c):
    return [idx for idx in range(len(numbers)) if is_adjacent_number(r, c, idx)]


with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

numbers, gears = [], []
for r, row in enumerate(grid):
    number, start_c = "", -1
    for c, ch in enumerate(row):
        if ch == "*":
            gears.append((r, c))
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


total = 0
for r, c in gears:
    indexes = set()
    for dr in DIRS:
        for dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc].isdigit():
                    indexes.update(get_adjacent_numbers(r, c))
    if len(indexes) == 2:
        _, _, n1 = numbers[indexes.pop()]
        _, _, n2 = numbers[indexes.pop()]
        total += int(n1) * int(n2)
print(total)  # 87449461
