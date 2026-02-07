#!/usr/bin/env python3

line = open(0).read().strip()

N = 14
for i in range(len(line) - N + 1):
    if len(set(line[i : i + N])) == N:
        print(i + N)  # 3559
        break
