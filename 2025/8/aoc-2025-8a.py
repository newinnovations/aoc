#!/usr/bin/env python3

import math
from itertools import combinations

filename, NUM = "input.txt", 1000


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def circuit_for_box(box):
    for i, circuit in enumerate(circuits):
        if box in circuit:
            return i
    return -1  # should not happen


boxes = list()
with open(filename) as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        boxes.append((x, y, z))

circuits = [[box] for box in boxes]

dists = [(distance(a, b), a, b) for a, b in combinations(boxes, 2)]
dists = sorted(dists, key=lambda x: x[0])

for _, a, b in dists[:NUM]:
    ca = circuit_for_box(a)
    cb = circuit_for_box(b)
    if ca != cb:
        circuits[ca] += circuits[cb]
        del circuits[cb]

lengths = sorted([len(c) for c in circuits])
total = 1
for length in lengths[-3:]:
    total *= length
print(total)  # 140008
