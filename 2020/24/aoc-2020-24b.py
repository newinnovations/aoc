#!/usr/bin/env python3

from collections import defaultdict

ALL_DIR = ["e", "w", "ne", "nw", "se", "sw"]


def neighbor(r, c, dir):
    if dir == "e":
        return r, c + 1
    elif dir == "w":
        return r, c - 1
    else:
        nr = r - 1 if dir[0] == "n" else r + 1
        nc = c + 1 if dir[1] == "e" else c
        return nr, nc - r % 2


def goto(dirs):
    r = c = 0
    for d in dirs:
        r, c = neighbor(r, c, d)
    return r, c


def tokenize(line):
    t = []
    while line:
        if line[0] in "ew":
            t.append(line[0])
            line = line[1:]
        else:
            t.append(line[:2])
            line = line[2:]
    return t


def run_day():
    global black_tiles
    white_tiles: set[tuple[int, int]] = set()
    black_to_remove: set[tuple[int, int]] = set()
    black_to_add: set[tuple[int, int]] = set()
    for bt in black_tiles:
        bn = set()
        for dir in ALL_DIR:
            n = neighbor(*bt, dir)
            if n in black_tiles:
                bn.add(n)
            else:
                white_tiles.add(n)
        if len(bn) > 2 or not bn:
            black_to_remove.add(bt)
    for wt in white_tiles:
        bn = set()
        for dir in ALL_DIR:
            n = neighbor(*wt, dir)
            if n in black_tiles:
                bn.add(n)
        if len(bn) == 2:
            black_to_add.add(wt)
    black_tiles -= black_to_remove
    black_tiles |= black_to_add


flipped = defaultdict(int)
with open(0) as f:
    for line in f:
        line = line.strip()
        flipped[goto(tokenize(line))] += 1

black_tiles: set[tuple[int, int]] = set(k for k, v in flipped.items() if v % 2)

for day in range(100):
    run_day()
    print(day + 1, len(black_tiles))  # 3665
