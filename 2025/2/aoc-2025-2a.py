#!/usr/bin/env python3

from itertools import batched

count = 0
with open("input.txt") as f:
    for pair in f.read().strip().split(","):
        start, finish = map(int, pair.split("-"))
        for id in range(start, finish + 1):
            id_str = str(id)
            if len(id_str) % 2 == 0:
                if len(set(batched(id_str, len(id_str) // 2))) == 1:
                    count += id
print(count)  # 38158151648
