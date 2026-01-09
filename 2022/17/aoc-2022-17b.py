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


def top_shape(g, shape, h, max_y):
    return tuple([g, shape] + [max_y - max(x) for x in h])


T = 1000000000000

gas = open(0).read().strip()
g = shape = rocks_stopped = 0
x, y = 2, 3
seen = dict()
skipped_height = 0
while True:
    dir = -1 if gas[g] == "<" else 1
    if fit(x + dir, y, shape, h):
        x += dir
    if fit(x, y - 1, shape, h):
        y -= 1
    else:
        rocks_stopped += 1
        place(x, y, shape, h)
        max_y = 1 + max(max(i) for i in h)
        if rocks_stopped == T:
            break
        if skipped_height == 0:
            ts = top_shape(g, shape, h, max_y)
            if ts in seen.keys():
                rep_start, max_start = seen[ts]
                repetition = rocks_stopped - rep_start
                remaining = T - rocks_stopped
                rep_times = remaining // repetition
                skipped_height = rep_times * (max_y - max_start)
                T -= rep_times * repetition
            else:
                seen[ts] = (rocks_stopped, max_y)
        x, y, shape = 2, max_y + 3, (shape + 1) % 5
    g = (g + 1) % len(gas)

print(max_y + skipped_height)  # 1565242165201
