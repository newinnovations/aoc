#!/usr/bin/env python3

from collections import defaultdict


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


flipped = defaultdict(int)
with open(0) as f:
    for line in f:
        line = line.strip()
        flipped[goto(tokenize(line))] += 1

print(sum(v % 2 for v in flipped.values()))  # 244
