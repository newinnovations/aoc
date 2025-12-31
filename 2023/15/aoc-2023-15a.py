#!/usr/bin/env python3


def hash(s):
    val = 0
    for ch in s:
        val += ord(ch)
        val *= 17
        val %= 256
    return val


with open("input.txt") as f:
    steps = f.read().strip().split(",")

print(sum(hash(s) for s in steps))  # 503154
