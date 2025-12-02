#!/usr/bin/env python3

total_joltage, N = 0, 12
with open("input.txt") as f:
    for line in f:
        b = [int(x) for x in line.strip()]
        joltage, start = 0, 0
        for n in range(N):
            max = -1
            for i in range(start, len(b) - N + n + 1):
                if b[i] > max:
                    start, max = i + 1, b[i]
            joltage = joltage * 10 + max
        total_joltage += joltage
print(total_joltage)  # 173229689350551
