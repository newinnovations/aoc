#!/usr/bin/env python3

import re


def follow_one(start, dir):
    if dir == "L":
        return nodes[start][0]
    return nodes[start][1]


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


start = "AAA"
count = 0
while True:
    start = follow(start)
    count += len(dirs)
    if start == "ZZZ":
        break
print(count)  # 14257
