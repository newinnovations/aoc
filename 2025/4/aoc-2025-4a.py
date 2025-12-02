#!/usr/bin/env python3


def paper(x, y):
    return x >= 0 and y >= 0 and x < size and y < size and area[y][x] == "@"


def can_remove(x, y):
    return area[y][x] == "@" and sum(paper(x + dx, y + dy) for dx in D for dy in D) < 5


with open("input.txt") as f:
    area = [list(line.strip()) for line in f]
D, size = [-1, 0, 1], len(area)
print(sum(can_remove(x, y) for x in range(size) for y in range(size)))  # 1346
