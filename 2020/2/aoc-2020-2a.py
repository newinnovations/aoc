#!/usr/bin/env python3

from re import compile

pattern = compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

valid = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        min_count, max_count, ch, password = pattern.findall(line)[0]
        count = len([c for c in password if c == ch])
        valid += int(min_count) <= count <= int(max_count)

print(valid)  # 528
