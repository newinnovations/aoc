#!/usr/bin/env python3

DIRS = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

rope = [[0, 0] for _ in range(10)]

hx, hy = tx, ty = (0, 0)
tail_pos = set(tuple([(tx, ty)]))


def follow_head(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        dx = max(-1, min(1, h[0] - t[0]))
        dy = max(-1, min(1, h[1] - t[1]))
        t[0], t[1] = t[0] + dx, t[1] + dy


with open(0) as f:
    for line in f:
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            dy, dx = DIRS[dir]
            rope[0][0] += dx
            rope[0][1] += dy
            for i in range(9):
                follow_head(rope[i], rope[i + 1])
            tail_pos.add(tuple(rope[9]))  # type: ignore

print(len(tail_pos))  # 2487
