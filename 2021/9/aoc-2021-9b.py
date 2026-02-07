#!/usr/bin/env python3


def get_low_spots():
    spots = set()
    for r in range(nrows):
        for c in range(ncols):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if grid[nr][nc] <= grid[r][c]:
                        break
            else:
                spots.add((r, c))
    return spots


def extend(r, c):
    s = set([(r, c)])
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols:
            if grid[nr][nc] < 9 and grid[nr][nc] > grid[r][c]:
                s.add((nr, nc))
                s.update(extend(nr, nc))
    return s


with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]
    nrows, ncols = len(grid), len(grid[0])

low_spots = get_low_spots()

bassins = []
for spot in low_spots:
    bassins.append(len(extend(*spot)))
bassins.sort()

total = 1
for n in bassins[-3:]:
    total *= n

print(total)  # 1075536
