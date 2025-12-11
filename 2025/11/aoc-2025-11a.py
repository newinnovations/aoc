#!/usr/bin/env python3


def count_path(start):
    if start == "out":
        return 1
    return sum(count_path(dev) for dev in devices[start])


devices = dict()
with open("input.txt") as f:
    for line in f:
        s = line.strip().split(": ")
        devices[s[0]] = s[1].split(" ")

print(count_path("you"))  # 636
