#!/usr/bin/env python3

DIRS = {
    "W": (-1, 0),
    "E": (1, 0),
    "N": (0, -1),
    "S": (0, 1),
}

ROT = "NESW"

dir = 1
x = y = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        action = line[0]
        amount = int(line[1:])
        if action in DIRS:
            dx, dy = DIRS[action]
            x, y = x + dx * amount, y + dy * amount
        elif action in ["L", "R"]:
            delta = amount // 90
            if action == "L":
                delta = -delta
            dir = (dir + delta) % 4
        elif action == "F":
            dx, dy = DIRS[ROT[dir]]
            x, y = x + dx * amount, y + dy * amount

print(abs(x) + abs(y))  # 1645
