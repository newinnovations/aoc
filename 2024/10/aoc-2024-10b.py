#!/usr/bin/env python3


def height(x, y):
    if x >= 0 and y >= 0 and x < size and y < size:
        return area[y][x]
    else:
        return -1


def num_trails(x, y, n):
    h = height(x, y)
    if h != n:
        return 0
    if n == 9:
        return 1
    return (
        num_trails(x + 1, y, n + 1)
        + num_trails(x - 1, y, n + 1)
        + num_trails(x, y + 1, n + 1)
        + num_trails(x, y - 1, n + 1)
    )


with open("input.txt") as f:
    area = [list(map(int, list(line.strip()))) for line in f]

size = len(area)
print(sum([num_trails(x, y, 0) for y in range(size) for x in range(size)]))  # 1801
