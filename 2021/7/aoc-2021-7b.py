#!/usr/bin/env python3


def cost(t, f):
    dist = abs(t - f)
    return (dist + 1) * dist // 2


def total_cost(n):
    return sum(cost(n, i) for i in pos)


total = 0
with open(0) as f:
    pos = list(map(int, f.read().split(",")))
pos.sort()

n = pos[len(pos) // 2]
delta = 1 if total_cost(n + 1) < total_cost(n) else -1

while True:
    c = total_cost(n)
    c2 = total_cost(n + delta)
    if c2 > c:
        print(c)  # 95519693
        break
    n += delta
