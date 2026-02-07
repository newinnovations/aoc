#!/usr/bin/env python3

from math import ceil, floor, sqrt


def num_wins(max_t, record_d):
    middle = max_t / 2
    delta = sqrt(max_t * max_t - 4 * record_d) / 2
    return 1 + ceil(middle + delta - 1) - floor(middle - delta + 1)


with open(0) as f:
    input = [line.strip().replace(" ", "").split(":") for line in f]
    times = list(map(int, input[0][1:]))
    dists = list(map(int, input[1][1:]))

total = 1
for t, d in zip(times, dists):
    total *= num_wins(t, d)
print(total)  # 29891250
