#!/usr/bin/env python3

with open("input.txt") as f:
    pebbles = f.readline().strip().split(" ")

lengths = dict()


def get_length(p, n):
    if n == 0:
        return 1
    if (p, n) in lengths.keys():
        return lengths[(p, n)]
    if p == "0":
        res = get_length("1", n - 1)
    elif (length := len(p)) % 2 == 0:
        res = get_length(str(int(p[: length // 2])), n - 1) + get_length(
            str(int(p[length // 2 :])), n - 1
        )
    else:
        res = get_length(str(int(p) * 2024), n - 1)
    lengths[(p, n)] = res
    return res


print(sum([get_length(p, 25) for p in pebbles]))  # 191690
print(sum([get_length(p, 75) for p in pebbles]))  # 228651922369703
