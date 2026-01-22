#!/usr/bin/env python3

with open(0) as f:
    dots, folds = f.read().split("\n\n")
    dots = [tuple(map(int, a.split(","))) for a in dots.split()]
    folds = [a.split("=") for a in folds.split() if "=" in a]
    folds = [(a, int(b)) for a, b in folds]


def do_fold(dots, axis, pos):
    ndots = set()
    for x, y in dots:
        if axis == "y" and y > pos:
            ndots.add((x, pos - (y - pos)))
        elif axis == "x" and x > pos:
            ndots.add((pos - (x - pos), y))
        else:
            ndots.add((x, y))
    return ndots


print(len(do_fold(dots, *folds[0])))  # 653
