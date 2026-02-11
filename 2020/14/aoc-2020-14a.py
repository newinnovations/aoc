#!/usr/bin/env python3

import re

pattern = re.compile(r"mem\[(\d+)\] = (\d+)")
mask0 = set()
mask1 = set()
memory = dict()
with open(0) as f:
    for line in f:
        line = line.strip()
        if line.startswith("mask = "):
            mask = line[7:]
            mask0 = {i for i, ch in enumerate(mask[::-1]) if ch == "0"}
            mask1 = {i for i, ch in enumerate(mask[::-1]) if ch == "1"}
        else:
            addr, data = map(int, pattern.findall(line)[0])
            b = bin(data)[2:]
            ba = {i for i, ch in enumerate(b[::-1]) if ch == "1"}
            ba |= mask1
            ba -= mask0
            ndata = sum(2**n for n in ba)
            memory[addr] = ndata

print(sum(memory.values()))  # 6386593869035
