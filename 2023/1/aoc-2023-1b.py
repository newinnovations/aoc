#!/usr/bin/env python3

N = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
with open(0) as f:
    for line in f:
        d = []
        for j in range(len(line)):
            if line[j].isdigit():
                d.append(int(line[j]))
            else:
                for i, n in enumerate(N):
                    if line[j:].startswith(n):
                        d.append(i + 1)
                        break
        total += d[0] * 10 + d[-1]
print(total)  # 55429
