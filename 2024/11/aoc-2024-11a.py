#!/usr/bin/env python3

with open("input.txt") as f:
    pebbles = f.readline().strip().split(" ")

for _ in range(25):
    next = list()
    for p in pebbles:
        if p == "0":
            next.append("1")
        elif (length := len(p)) % 2 == 0:
            next.append(str(int(p[: length // 2])))
            next.append(str(int(p[length // 2 :])))
        else:
            next.append(str(int(p) * 2024))
    pebbles = next
print(len(pebbles))  # 191690
