#!/usr/bin/env python3

from functools import cache


@cache
def count_fish(age, days):
    if days == 0:
        return 1
    if age == 0:
        return count_fish(6, days - 1) + count_fish(8, days - 1)
    return count_fish(age - 1, days - 1)


N = 256
total = 0
with open(0) as f:
    fish = list(map(int, f.read().split(",")))

for age in fish:
    total += count_fish(age, N)
print(total)  # 1632146183902
