#!/usr/bin/env python3

h = [set([-1]) for _ in range(7)]

SHAPES = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
]


def fit(x, y, shape, h):
    for dx, dy in SHAPES[shape]:
        if not 0 <= x + dx < 7:
            return False
        if y + dy in h[x + dx]:
            return False
    return True


def place(x, y, shape, h):
    for dx, dy in SHAPES[shape]:
        h[x + dx].add(y + dy)


gas = open(0).read().strip()
g = shape = rocks_stopped = 0
x, y = 2, 3
while True:
    dir = -1 if gas[g] == "<" else 1
    if fit(x + dir, y, shape, h):
        x += dir
    if fit(x, y - 1, shape, h):
        y -= 1
    else:
        place(x, y, shape, h)
        max_y = 1 + max(max(i) for i in h)
        rocks_stopped += 1
        if rocks_stopped == 2022:
            break
        x, y, shape = 2, max_y + 3, (shape + 1) % 5
    g = (g + 1) % len(gas)

print(max_y)  # 3144
