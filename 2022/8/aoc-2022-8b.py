#!/usr/bin/env python3


def num_visible(r, c, dr, dc):
    n = area[r][c]
    total = 0
    while True:
        r, c = r + dr, c + dc
        if not (0 <= r < nrows and 0 <= c < ncols):
            return total
        total += 1
        if area[r][c] >= n:
            return total


def scenic_score(r, c):
    score = 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        score *= num_visible(r, c, dr, dc)
    return score


with open(0) as f:
    area = [list(map(int, list(line.strip()))) for line in f]
    nrows, ncols = len(area), len(area[0])

print(max(scenic_score(r, c) for r in range(nrows) for c in range(ncols)))  # 517440
