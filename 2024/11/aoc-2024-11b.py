#!/usr/bin/env python3

from functools import cache


@cache
def get_length(p, n):
    if n == 0:
        return 1
    if p == "0":
        return get_length("1", n - 1)
    if (length := len(p)) % 2 == 0:
        return get_length(str(int(p[: length // 2])), n - 1) + get_length(
            str(int(p[length // 2 :])), n - 1
        )
    return get_length(str(int(p) * 2024), n - 1)


with open("input.txt") as f:
    pebbles = f.readline().strip().split(" ")


# print(sum([get_length(p, 25) for p in pebbles]))  # 191690
print(sum([get_length(p, 75) for p in pebbles]))  # 228651922369703
