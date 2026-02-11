#!/usr/bin/env python3

import re
from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


pattern = re.compile(r"mem\[(\d+)\] = (\d+)")
mask1 = set()
maskx = set()
mask_adds = list()
memory = dict()
with open(0) as f:
    for line in f:
        line = line.strip()
        if line.startswith("mask = "):
            mask = line[7:]
            mask1 = {i for i, ch in enumerate(mask[::-1]) if ch == "1"}
            maskx = {i for i, ch in enumerate(mask[::-1]) if ch == "X"}
            mask_adds = [sum(2**n for n in ps) for ps in powerset(maskx)]
        else:
            addr, data = map(int, pattern.findall(line)[0])
            b = bin(addr)[2:]
            ba = {i for i, ch in enumerate(b[::-1]) if ch == "1"}
            ba |= mask1
            ba -= maskx
            naddr = sum(2**n for n in ba)
            for a in mask_adds:
                memory[a + naddr] = data

print(sum(memory.values()))  # 4288986482164
