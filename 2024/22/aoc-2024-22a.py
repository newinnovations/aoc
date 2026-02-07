#!/usr/bin/env python3

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


numbers = []
with open(0) as f:
    numbers = [int(line) for line in f]

total = 0
for seed in numbers:
    for _ in range(2000):
        seed = next_secret(seed)
    total += seed
print(total)  # 17163502021
