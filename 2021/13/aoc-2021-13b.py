#!/usr/bin/env python3

with open(0) as fold:
    dots, folds = fold.read().split("\n\n")
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


for fold in folds:
    dots = do_fold(dots, *fold)

xl = yl = int(1e8)
xh = yh = -int(1e8)
for x, y in dots:
    xl = min(xl, x)
    yl = min(yl, y)
    xh = max(xh, x)
    yh = max(yh, y)

viz = [[" " for _ in range(xh - xl + 1)] for _ in range(yh - yl + 1)]

for x, y in dots:
    viz[y - yl][x - xl] = "#"

#    #    #  # ###  #### ###  ###  ###  #  #
#    #    # #  #  # #    #  # #  # #  # # #
#    #    ##   #  # ###  ###  #  # #  # ##
#    #    # #  ###  #    #  # ###  ###  # #
#    #    # #  # #  #    #  # #    # #  # #
#    #### #  # #  # #### ###  #    #  # #  #
for row in viz:
    print("".join(row))  # LKREBPRK
