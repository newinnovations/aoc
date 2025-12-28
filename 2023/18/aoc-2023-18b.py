#!/usr/bin/env python3

from shapely import Polygon

F = "input.txt"
input = [f.strip().split(" ") for f in open(F).readlines()]

outline, x, y = [], 0, 0
for _, _, h in input:
    length = int(h[2:7], 16)
    match h[7]:
        case "0":
            x += length
        case "1":
            y += length
        case "2":
            x -= length
        case "3":
            y -= length
    outline.append((x, y))

polygon = Polygon(outline)

# Buffer by 0.5 to expand the polygon to cover the grid squares
buffered = polygon.buffer(0.5, join_style="mitre")
print(buffered.area)  # 48652

# Pick's theorem
print(polygon.area + polygon.length / 2 + 1)

# Area can also be calculated by the shoelace formula / Gauss's area formula
