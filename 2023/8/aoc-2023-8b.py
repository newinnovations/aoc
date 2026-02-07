#!/usr/bin/env python3

import re
from functools import cache
from math import lcm

"""
LCM: Least Common Multiple (LCM)

For many inputs (including the well-known puzzle this resembles), each start hits a *Z at block boundary time t_i,
and then every t_i blocks thereafter. In other words, the period equals the first hit. Then the overall answer is:
answer_steps = lcm(t_1, t_2, ..., t_k) * len(dirs)
"""


def follow_one(start, dir):
    if dir == "L":
        return nodes[start][0]
    return nodes[start][1]


@cache
def follow(start):
    # apply one full block of directions
    cur = start
    for d in dirs:
        cur = follow_one(cur, d)
    return cur


def blocks_to_first_Z(start):
    """Return number of blocks until we first land on a *Z node at a block boundary."""
    cur = start
    steps = 0
    seen = set()
    while True:
        if cur[2] == "Z":
            return steps  # number of full dir-blocks
        if cur in seen:
            raise RuntimeError(f"No Z reachable at block boundaries from {start}")
        seen.add(cur)
        cur = follow(cur)
        steps += 1


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

starts = [k for k in nodes if k.endswith("A")]

# Compute, per start, in how many blocks we first land on *Z
block_hits = [blocks_to_first_Z(s) for s in starts]

# Combine with LCM; each block represents len(dirs) single-step moves
blocks_lcm = 1
for t in block_hits:
    blocks_lcm = lcm(blocks_lcm, t)

answer_steps = blocks_lcm * len(dirs)
print(answer_steps)  # 16187743689077
