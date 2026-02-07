#!/usr/bin/env python3

with open(0) as f:
    area = [list(line.strip()) for line in f]

size = len(area)
start_x, start_y = 0, 0
for start_y in range(size):
    if "^" in area[start_y]:
        start_x = area[start_y].index("^")
        break

total, x, y, dir, dx, dy = 0, start_x, start_y, "up", 0, -1
while True:
    if area[y][x] != "X":
        area[y][x] = "X"
        total += 1
    next_x, next_y = x + dx, y + dy
    if next_x < 0 or next_y < 0 or next_x >= size or next_y >= size:
        break
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
print(total)  # 5461
