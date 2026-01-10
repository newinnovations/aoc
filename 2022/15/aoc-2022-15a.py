#!/usr/bin/env python3
import re

# Ranges here are [start, finish)  [10,20) and [20,30) touch but do not overlap


def get_range_at_y(y, sx, sy, bx, by):
    dist = abs(sx - bx) + abs(sy - by)
    d = dist - abs(y - sy)
    if d >= 0:
        return (sx - d, sx + d + 1)
    return None


def compact_ranges(ranges):  # new and improved
    compact = []
    for start, finish in sorted(ranges):
        if finish > start:
            if not compact:
                compact.append((start, finish))
            else:
                last_start, last_finish = compact[-1]
                if start > last_finish:
                    compact.append((start, finish))
                else:
                    compact[-1] = (last_start, max(last_finish, finish))
    return compact


with open(0) as f:
    data = [list(map(int, re.findall(r"=([-\d]+)", line.strip()))) for line in f]

Y = 2000000 if len(data) > 15 else 10
occupied = set()
ranges = []
for sx, sy, bx, by in data:
    if by == Y:
        occupied.add((bx, by))
    range = get_range_at_y(Y, sx, sy, bx, by)
    if range:
        ranges.append(range)
print(sum(b - a for a, b in compact_ranges(ranges)) - len(occupied))  # 5166077
