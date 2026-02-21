#!/usr/bin/env python3

from re import compile

pattern = compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

valid = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        pos1, pos2, ch, password = pattern.findall(line)[0]
        ch1 = password[int(pos1) - 1]
        ch2 = password[int(pos2) - 1]
        valid += (ch1 == ch and ch2 != ch) or (ch1 != ch and ch2 == ch)

print(valid)  # 497
