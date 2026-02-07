#!/usr/bin/env python3


def num_wins(max_t, record_d):
    count = 0
    for t in range(max_t + 1):
        d = t * (max_t - t)
        count += d > record_d
    return count


with open(0) as f:
    input = [line.strip().split() for line in f]
    times = list(map(int, input[0][1:]))
    dists = list(map(int, input[1][1:]))

total = 1
for t, d in zip(times, dists):
    total *= num_wins(t, d)
print(total)  # 2612736
