#!/usr/bin/env python3


def adjacent(seat):
    r, c = seat
    return [
        (r + dr, c + dc)
        for dr in [-1, 0, 1]
        for dc in [-1, 0, 1]
        if not (dr == 0 and dc == 0)
    ]


total = 0
with open(0) as f:
    grid = [list(line.strip()) for line in f]

seats = {(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "L"}
occupied = set()

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

step = 0
while True:
    step += 1

    to_occupy = set()
    for seat in seats - occupied:
        if not (any(a in occupied for a in adjacent(seat))):
            to_occupy.add(seat)

    to_vacate = set()
    for seat in occupied:
        num_occupied = sum(a in occupied for a in adjacent(seat))
        if num_occupied >= 4:
            to_vacate.add(seat)

    if not to_occupy and not to_vacate:
        # print(step)
        print(len(occupied))  # 2329
        break

    occupied -= to_vacate
    occupied.update(to_occupy)
