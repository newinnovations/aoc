#!/usr/bin/env python3

from collections import defaultdict


def rotate(rot, p):
    res = list(p)

    xpos = rot % 3
    ypos = 1 if xpos == 0 else 0
    zpos = 1 if xpos == 2 else 2

    if xpos != 0:
        res[xpos] = p[0]
        res[ypos] = -p[xpos]

    if (rot // 3) % 2:
        res[xpos] = -res[xpos]
        res[ypos] = -res[ypos]

    rot_yz = rot // 6
    if rot_yz == 1:
        ra, rb = res[zpos], -res[ypos]
    elif rot_yz == 2:
        ra, rb = -res[ypos], -res[zpos]
    elif rot_yz == 3:
        ra, rb = -res[zpos], res[ypos]
    else:
        ra, rb = res[ypos], res[zpos]
    res[ypos], res[zpos] = ra, rb

    return tuple(res)


def overlap(rot2, scanner1, scanner2, pos1):
    diffs = defaultdict(int)
    for b2 in scanner2:
        b2 = rotate(rot2, b2)
        for b1 in scanner1:
            d = tuple(a + b - c for a, b, c in zip(pos1, b1, b2))
            diffs[d] += 1
    for k, v in diffs.items():
        if v > 11:
            return k


total = 0
with open(0) as f:
    scanners = f.read().split("\n\n")
scanners = [s.splitlines()[1:] for s in scanners]
scanners = [[tuple(map(int, b.split(","))) for b in s] for s in scanners]

unknown_rotations = [s != 0 for s in range(len(scanners))]
positions = [(0, 0, 0) for _ in range(len(scanners))]

while any(unknown_rotations):
    for s1, scanner1 in enumerate(scanners):
        if unknown_rotations[s1]:
            continue
        for s2, scanner2 in enumerate(scanners):
            if not unknown_rotations[s2]:
                continue
            for rot in range(24):
                pos = overlap(rot, scanner1, scanner2, positions[s1])
                if pos:
                    positions[s2] = pos
                    unknown_rotations[s2] = False
                    scanners[s2] = [rotate(rot, b) for b in scanners[s2]]
                    break

# print(rotations)
# print(positions)

beacons = set()
for s, scanners in enumerate(scanners):
    for beacon in scanners:
        beacon = tuple(a + b for a, b in zip(beacon, positions[s]))
        beacons.add(beacon)

print(len(beacons))  # 390
