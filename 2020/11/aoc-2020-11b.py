#!/usr/bin/env python3

from functools import cache


@cache
def los(seat):
    r, c = seat
    result = set()
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr, c + dc)
            while 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in seats:
                nr, nc = (nr + dr, nc + dc)
            if (nr, nc) in seats:
                result.add((nr, nc))
    return result


# def dump():
#     for r in range(nrows):
#         for c in range(ncols):
#             if (r, c) in occupied:
#                 print("#", end="")
#             elif (r, c) in seats:
#                 print("L", end="")
#             else:
#                 print(".", end="")
#         print()
#     print()


total = 0
with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

seats = {(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "L"}
occupied = set()

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

while True:
    to_occupy = set()
    for seat in seats - occupied:
        if not (any(a in occupied for a in los(seat))):
            to_occupy.add(seat)

    to_vacate = set()
    for seat in occupied:
        num_occupied = sum(a in occupied for a in los(seat))
        if num_occupied >= 5:
            to_vacate.add(seat)

    if not to_occupy and not to_vacate:
        print(len(occupied))  # 2138
        break

    occupied -= to_vacate
    occupied.update(to_occupy)
    occupied.update(to_occupy)
