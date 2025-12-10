#!/usr/bin/env python3

from itertools import pairwise

robots = list()
with open("input.txt") as f:
    for line in f:
        px, py, vx, vy = map(
            int, line.strip().replace("p=", "").replace(" v=", ",").split(",")
        )
        robots.append([px, py, vx, vy])

W, H = 101, 103

step = 1
while True:
    end_state = [
        [(px + step * vx) % W, (py + step * vy) % H] for px, py, vx, vy in robots
    ]
    indexes = sorted([w + W * h for w, h in end_state])
    num_conseq = sum([i2 == i1 + 1 for i1, i2 in pairwise(indexes)])
    if num_conseq > 100:
        print(step)  # 8159
        break
    step += 1

for h in range(H):
    for w in range(W):
        count = any(h == y and w == x for x, y in end_state)
        print("#" if count else ".", end="")
    print()
