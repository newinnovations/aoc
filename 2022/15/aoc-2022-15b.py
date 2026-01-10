#!/usr/bin/env python3
import re

# Ranges here are [start, finish)  [10,20) and [20,30) touch but do not overlap


def get_range_at_y(y, sx, sy, bx, by):
    dist = abs(sx - bx) + abs(sy - by)
    d = dist - abs(y - sy)
    if d >= 0:
        return (max(0, sx - d), 1 + min(MAX, sx + d))
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

MAX = 4000000 if len(data) > 15 else 20

for y in range(MAX + 1):
    ranges = []
    for sx, sy, bx, by in data:
        range = get_range_at_y(y, sx, sy, bx, by)
        if range:
            ranges.append(range)
    ranges = compact_ranges(ranges)
    if len(ranges) != 1:
        _, x = ranges[0]
        print(x * 4000000 + y)  # 13071206703981 (30 seconds)
        break
