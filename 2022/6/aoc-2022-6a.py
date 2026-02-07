#!/usr/bin/env python3

line = open(0).read().strip()

for i in range(len(line) - 3):
    if len(set(line[i : i + 4])) == 4:
        print(i + 4)  # 1702
        break
