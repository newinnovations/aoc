#!/usr/bin/env python3

from functools import cache


@cache
def count_path(start, target):
    if start == target:
        return 1
    return sum(count_path(dev, target) for dev in devices[start])


devices = dict()
with open("input.txt") as f:
    for line in f:
        s = line.strip().split(": ")
        devices[s[0]] = s[1].split(" ")
devices["out"] = []

print(
    count_path("svr", "fft") * count_path("fft", "dac") * count_path("dac", "out")
    + count_path("svr", "dac") * count_path("dac", "fft") * count_path("fft", "out")
)  # 509312913844956

# NOTE: there is no path from "dac" to "fft" which makes sense :-)
#       so the second term is zero
