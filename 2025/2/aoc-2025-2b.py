#!/usr/bin/env python3

from itertools import batched

count = 0
with open("input.txt") as f:
    for pair in f.read().strip().split(","):
        start, finish = map(int, pair.split("-"))
        for id in range(start, finish + 1):
            id_str = str(id)
            for chunk_size in range(1, len(id_str) // 2 + 1):
                if len(set(batched(id_str, chunk_size))) == 1:
                    count += id
                    break
print(count)  # 45283684555
