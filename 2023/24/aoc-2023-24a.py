#!/usr/bin/env python3

from itertools import combinations

# MIN, MAX, FILENAME = 7, 27, "ref.txt"
MIN, MAX, FILENAME = 200000000000000, 400000000000000, "input.txt"


def intersect(a, b):
    """
    x = apx + avx * ta = bpx + bvx * tb
    y = apy + avy * ta = bpy + bvy * tb

    apx * avy + avx * avy * ta = bpx * avy + bvx * avy * tb
    apy * avx + avx * avy * ta = bpy * avx + bvy * avx * tb

    (apx * avy - apy * avx) = (bpx * avy - bpy * avx) + (bvx * avy - bvy * avx) * tb

    (bvx * avy - bvy * avx) * tb = ((apx * avy - apy * avx) - (bpx * avy - bpy * avx))

    tb = ((apx * avy - apy * avx) - (bpx * avy - bpy * avx)) / (bvx * avy - bvy * avx)
    """
    apx, apy, _, avx, avy, _ = a
    bpx, bpy, _, bvx, bvy, _ = b
    denom = bvx * avy - bvy * avx
    if denom:
        tb = ((apx * avy - apy * avx) - (bpx * avy - bpy * avx)) / denom
        if tb < 0:
            return False  # tb in the past
        x = bpx + bvx * tb
        if x < MIN or x > MAX:
            return False  # x ouside range
        y = bpy + bvy * tb
        if y < MIN or y > MAX:
            return False  # y ouside range
        ta = (x - apx) / avx
        if ta < 0:
            return False  # ta in the past
        return True  # all is well
    else:
        return False  # parallel / no intersection


particles = []
with open(FILENAME) as f:
    for line in f:
        px, py, pz, vx, vy, vz = map(
            int, line.strip().replace(" ", "").replace("@", ",").split(",")
        )
        particles.append((px, py, pz, vx, vy, vz))

print(sum(intersect(a, b) for a, b in combinations(particles, 2)))  # 15107
