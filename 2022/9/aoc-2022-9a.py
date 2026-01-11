#!/usr/bin/env python3

DIRS = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

hx, hy = tx, ty = (0, 0)
tail_pos = set([(tx, ty)])

with open(0) as f:
    for line in f:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            dy, dx = DIRS[dir]
            hx, hy = hx + dx, hy + dy
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                dx = max(-1, min(1, hx - tx))
                dy = max(-1, min(1, hy - ty))
                tx, ty = tx + dx, ty + dy
            tail_pos.add((tx, ty))

print(len(tail_pos))  # 6081
