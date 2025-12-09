#!/usr/bin/env python3

"""
x = xa * a + xb * b
y = ya * a + yb * b

x * ya = xa * ya * a + xb * ya * b
y * xa = xa * ya * a + xa * yb * b

(x * ya - y * xa) = (xb * ya - xa * yb) * b

b = (x * ya - y * xa) / (xb * ya - xa * yb)
"""


def solve(x, xa, xb, y, ya, yb):
    if (x * ya - y * xa) % (xb * ya - xa * yb) != 0:
        return None
    b = (x * ya - y * xa) // (xb * ya - xa * yb)
    if (x - xb * b) % xa != 0:
        return None
    a = (x - xb * b) // xa
    return a * 3 + b


total, xa, xb, ya, yb = 0, 0, 0, 0, 0
with open("input.txt") as f:
    for line in f:
        if line.startswith("Button A: X+"):
            xa, ya = map(int, line[12:].split(", Y+"))
        if line.startswith("Button B: X+"):
            xb, yb = map(int, line[12:].split(", Y+"))
        if line.startswith("Prize: X="):
            x, y = map(int, line[9:].split(", Y="))
            if cost := solve(10000000000000 + x, xa, xb, 10000000000000 + y, ya, yb):
                total += cost
print(total)  # 92871736253789
