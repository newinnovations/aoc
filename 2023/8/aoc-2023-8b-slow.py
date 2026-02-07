#!/usr/bin/env python3

import re
from functools import cache


def follow_one(start, dir):
    if dir == "L":
        return nodes[start][0]
    return nodes[start][1]


@cache
def follow(start):
    for dir in dirs:
        start = follow_one(start, dir)
    return start


nodes = {}
dirs, pattern = [], re.compile(r"(...) = \((...), (...)\)")
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            if match := pattern.match(line):
                node, left, right = match.groups()
                nodes[node] = (left, right)
            else:
                dirs = list(line)


starts = [k for k in nodes.keys() if k[2] == "A"]
ends = [k for k in nodes.keys() if k[2] == "Z"]

print(starts, len(starts))
print(ends, len(ends))

count = 0
while True:
    starts = [follow(s) for s in starts]
    count += len(dirs)
    if all(s[2] == "Z" for s in starts):
        break
print(count)
