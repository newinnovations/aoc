#!/usr/bin/env python3

from collections import defaultdict
from itertools import pairwise

MOD = 1 << 24  # 16777216
MASK = MOD - 1  # 0xFFFFFF


def next(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


def next_secret(seed: int) -> int:
    """Return the next 24-bit value from the custom PRNG state."""
    seed ^= (seed << 6) & MASK  # multiply by 64
    seed ^= (seed >> 5) & MASK  # integer divide by 32
    seed ^= (seed << 11) & MASK  # multiply by 2048
    return seed & MASK


def sequence(seed, N):
    result = []
    for _ in range(N):
        result.append(seed % 10)
        seed = next_secret(seed)
    return result


numbers = []
with open(0) as f:
    numbers = [int(line) for line in f]

all = defaultdict(int)
for seed in numbers:
    s = sequence(seed, 2000)
    seen = set()
    for i in range(len(s) - 5):
        q = s[i : i + 5]
        d = tuple([a - b for a, b in pairwise(q)])
        if d not in seen:
            all[d] += q[-1]
            seen.add(d)

print(max(all.values()))  # 1938
