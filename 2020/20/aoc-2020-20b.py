#!/usr/bin/env python3

from collections import defaultdict


def rotate(g, r):
    if r & 4:
        g = ["".join(a) for a in zip(*g)]
    if r & 2:
        g = [a[::-1] for a in g]
    if r & 1:
        g = g[::-1]
    return g


def tblr(g):
    t = rotate(g, 4)
    return g[0], g[-1], t[0], t[-1]


TILES, EDGES = dict(), dict()
with open(0) as f:
    data = f.read().split("\n\n")
    for tile_data in data:
        tile_data = tile_data.splitlines()
        if not tile_data:
            break
        tile_no, tile = int(tile_data[0][5:-1]), tile_data[1:]
        TILES[tile_no] = tile
        EDGES[tile_no] = set(rotate(tile, r)[0] for r in range(8))


# for k, v in T.items():
#     print(k, v)

C = defaultdict(set)
for k1, v1 in EDGES.items():
    for k2, v2 in EDGES.items():
        if k1 != k2:
            if v1 & v2:
                C[k1].add(k2)

corners = []
for k, v in C.items():
    if len(v) == 2:
        corners.append(k)
# print("corners:", corners)


def find_nb(a, b, placed):
    result = None
    for a1 in C[a] - placed:
        for b1 in C[b] - placed:
            if a1 in C[b1]:
                assert result is None
                result = (a1, b1)
                placed.update([a1, b1])
    return result


n0 = corners[0]
n1, n2 = C[n0].pop(), C[n0].pop()
placed = set([n0, n1, n2])
n3 = (C[n1] & C[n2]) - (placed)
assert len(n3) == 1
n3 = n3.pop()
placed.add(n3)

tile = [[corners[0], n1], [n2, n3]]
while res := find_nb(tile[0][-1], tile[1][-1], placed):
    tile[0].append(res[0])
    tile[1].append(res[1])

while res := find_nb(tile[-1][0], tile[-1][1], placed):
    a, b = res
    tile.append([a, b])
    for a in tile[-2][2:]:
        b = (C[a] & C[b]) - (placed)
        assert len(b) == 1
        b = b.pop()
        placed.add(b)
        tile[-1].append(b)

# for row in tile:
#     print(row)


def find_rot_options(t1, t2, hor):
    res = set()
    for r1 in range(8):
        for r2 in range(8):
            tblr1 = tblr(rotate(TILES[t1], r1))
            tblr2 = tblr(rotate(TILES[t2], r2))
            if hor:
                if tblr1[3] == tblr2[2]:
                    res.add(r1)
            else:
                if tblr1[1] == tblr2[0]:
                    res.add(r1)
    return res


def find_rot(t1, t2, hor):
    res = set()
    tblr1 = tblr(TILES[t1])
    for r2 in range(8):
        tblr2 = tblr(rotate(TILES[t2], r2))
        if hor:
            if tblr1[3] == tblr2[2]:
                res.add(r2)
        else:
            if tblr1[1] == tblr2[0]:
                res.add(r2)
    assert len(res) == 1
    return res.pop()


rot_0_0 = find_rot_options(tile[0][0], tile[1][0], False) & find_rot_options(
    tile[0][0], tile[0][1], True
)
assert len(rot_0_0) == 1
TILES[tile[0][0]] = rotate(TILES[tile[0][0]], rot_0_0.pop())
for r in range(1, len(tile)):
    rot = find_rot(tile[r - 1][0], tile[r][0], False)
    TILES[tile[r][0]] = rotate(TILES[tile[r][0]], rot)
for r in range(len(tile)):
    for c in range(1, len(tile[0])):
        rot = find_rot(tile[r][c - 1], tile[r][c], True)
        TILES[tile[r][c]] = rotate(TILES[tile[r][c]], rot)

combined = []
for row in tile:
    for r in range(1, len(TILES[row[0]]) - 1):
        line = ""
        for col in row:
            line += TILES[col][r][1:-1]
        combined.append(line)

monster = ["                  #", "#    ##    ##    ###", " #  #  #  #  #  #"]
monster = [
    (r, c) for r, row in enumerate(monster) for c, ch in enumerate(row) if ch == "#"
]


for rot in range(8):
    matched = set()
    comrot = rotate(combined, rot)
    for r in range(len(comrot) - 2):
        for c in range(len(comrot[0]) - 19):
            if all(comrot[r + dr][c + dc] == "#" for dr, dc in monster):
                for dr, dc in monster:
                    matched.add((r + dr, c + dc))
    if matched:
        total = {
            (r, c)
            for r, row in enumerate(comrot)
            for c, ch in enumerate(row)
            if ch == "#"
        }
        print(len(total - matched))  # 1555
