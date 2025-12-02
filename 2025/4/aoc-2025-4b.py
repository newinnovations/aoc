#!/usr/bin/env python3


def paper(x, y):
    return x >= 0 and y >= 0 and x < size and y < size and area[y][x] == "@"


def can_remove(x, y):
    return area[y][x] == "@" and sum(paper(x + dx, y + dy) for dx in D for dy in D) < 5


def remove_paper():
    to_remove = [(x, y) for x in range(size) for y in range(size) if can_remove(x, y)]
    for x, y in to_remove:
        area[y][x] = "x"
    return len(to_remove)


with open("input.txt") as f:
    area = [list(line.strip()) for line in f]
D, size, total = [-1, 0, 1], len(area), 0
while removed := remove_paper():
    total += removed
print(total)  # 8493
