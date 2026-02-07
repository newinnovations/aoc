#!/usr/bin/env python3

import copy


def is_loop(area, start_x, start_y):
    x, y, dir, dx, dy = start_x, start_y, "up", 0, -1
    while True:
        if dir in area[y][x]:
            return True
        area[y][x] += dir
        next_x, next_y = x + dx, y + dy
        if next_x < 0 or next_y < 0 or next_x >= size or next_y >= size:
            return False
        elif area[next_y][next_x] == "#":
            if dir == "up":
                dir, dx, dy = "right", 1, 0
            elif dir == "right":
                dir, dx, dy = "down", 0, 1
            elif dir == "down":
                dir, dx, dy = "left", -1, 0
            elif dir == "left":
                dir, dx, dy = "up", 0, -1
        else:
            x, y = next_x, next_y


with open(0) as f:
    area_orig = [list(line.strip()) for line in f]

size = len(area_orig)
start_x, start_y = 0, 0
for start_y in range(size):
    if "^" in area_orig[start_y]:
        start_x = area_orig[start_y].index("^")
        break

total = 0
for x in range(size):
    for y in range(size):
        if area_orig[y][x] == ".":
            area = copy.deepcopy(area_orig)
            area[y][x] = "#"
            total += is_loop(area, start_x, start_y)
print(total)  # 1836
