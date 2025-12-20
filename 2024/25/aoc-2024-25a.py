#!/usr/bin/env python3

LOCKS, KEYS = [], []


def add_shape(shape):
    global LOCKS, KEYS
    sig = [len([x for x in s if x == "#"]) - 1 for s in zip(*shape)]
    if shape[0][0] == "#":
        LOCKS.append(sig)
    else:
        KEYS.append(sig)


def check_fit():
    total_fit = 0
    for lock in LOCKS:
        for key in KEYS:
            sum = [a + b for a, b in zip(lock, key)]
            fit = all(s < 6 for s in sum)
            # print(lock, key, fit, sum)
            total_fit += fit
    print(total_fit)  # 3264


with open("input.txt") as f:
    shape = []
    for line in f:
        line = line.strip()
        if not line:
            add_shape(shape)
            shape = []
        else:
            shape.append(list(line))
    add_shape(shape)
