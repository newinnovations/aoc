#!/usr/bin/env python3


from functools import cache


@cache
def count_path(start, seen_fft, seen_dac):
    if start == "out":
        return int(seen_fft and seen_dac)
    seen_fft = seen_fft or start == "fft"
    seen_dac = seen_dac or start == "dac"
    return sum(count_path(dev, seen_fft, seen_dac) for dev in devices[start])


devices = dict()
with open("input.txt") as f:
    for line in f:
        s = line.strip().split(": ")
        devices[s[0]] = s[1].split(" ")

print(count_path("svr", False, False))  # 509312913844956
