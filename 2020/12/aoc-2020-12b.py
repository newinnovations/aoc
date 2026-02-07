#!/usr/bin/env python3

DIRS = {
    "W": (-1, 0),
    "E": (1, 0),
    "N": (0, -1),
    "S": (0, 1),
}

wx, wy = 10, -1
x, y = 0, 0
with open(0) as f:
    for line in f:
        line = line.strip()
        action = line[0]
        amount = int(line[1:])
        if action in DIRS:
            dx, dy = DIRS[action]
            wx, wy = wx + dx * amount, wy + dy * amount
        elif action in ["L", "R"]:
            delta = amount // 90
            if action == "L":
                delta = -delta
            delta = delta % 4
            if delta == 1:
                wx, wy = -wy, wx
            elif delta == 2:
                wx, wy = -wx, -wy
            elif delta == 3:
                wx, wy = wy, -wx
        elif action == "F":
            x, y = x + wx * amount, y + wy * amount


print(abs(x) + abs(y))  # 35292
