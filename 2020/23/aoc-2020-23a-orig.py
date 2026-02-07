#!/usr/bin/env python3

with open(0) as f:
    cups = list(map(int, f.read().strip()))

current = cups[0]

N = len(cups)

for step in range(100):
    take = []
    p = cups.index(current) + 1
    for i in range(3):
        if p >= len(cups):
            p = 0
        take.append(cups[p])
        del cups[p]
    destination = current - 1
    while destination not in cups:
        if destination <= 1:
            destination = N
        else:
            destination -= 1
    dest_idx = cups.index(destination)
    cups = cups[: dest_idx + 1] + take + cups[dest_idx + 1 :]
    next_idx = cups.index(current) + 1
    if next_idx >= N:
        next_idx = 0
    current = cups[next_idx]

idx = cups.index(1)
for i in range(1, N):
    print(cups[(i + idx) % N], end="")
print()  # 78569234
