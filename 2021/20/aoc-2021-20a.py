#!/usr/bin/env python3


def calc_offset(r, c):
    offset = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            offset *= 2
            nr, nc = r + dr, c + dc
            if rl <= nr <= rh and cl <= nc <= ch:
                offset += (nr, nc) in pixels
            elif mask[0] == "#":
                offset += step % 2 == 1
    return offset


def extend():
    rl = rh = cl = ch = 0
    for r, c in pixels:
        rl, cl, rh, ch = min(r, rl), min(c, cl), max(r, rh), max(c, ch)
    return rl, rh, cl, ch


total = 0
pixels = set()
with open(0) as f:
    mask, data = f.read().split("\n\n")
    assert len(mask) == 512
    for r, row in enumerate(data.splitlines()):
        for c, ch in enumerate(row):
            if ch == "#":
                pixels.add((r, c))


rl, rh, cl, ch = extend()
for step in range(2):
    npixels = set()
    for r in range(rl - 1, rh + 2):
        for c in range(cl - 1, ch + 2):
            offset = calc_offset(r, c)
            if mask[offset] == "#":
                npixels.add((r, c))
    pixels = npixels
    rl, rh, cl, ch = rl - 1, rh + 1, cl - 1, ch + 1

print(len(pixels))  # 5486
