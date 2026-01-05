#!/usr/bin/env python3

import re

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
R, D, L, U = 0, 1, 2, 3
E, S, W, N = R, D, L, U
DIR = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRV = ">v<^"

# .N.................................  1 N -> 9 W no flip
# W.E..........A-----B-----C.........  1 W -> 6 W flip
# .S........0..|  1  |  2  |.........  2 N -> 9 S no flip
# .............|     |     |.........  2 E -> 7 E flip
# .............D-----E-----F.........  6 N -> 4 W no flip
# ..........3..|  4  |..5............  2 S -> 4 E no flip
# .............|     |...............  7 S -> 9 E no flip
# .......D-----G-----F...............  9 W -> 1 N no flip
# .......|  6  |  7  |..8............  6 W -> 1 W flip
# .......|     |     |...............  9 S -> 2 N no flip
# .......A-----H-----C...............  7 E -> 2 E flip
# .......|  9  |..10....11...........  4 W -> 6 N no flip
# .......|     |.....................  4 E -> 2 S no flip
# .......B-----C.....................  9 E -> 7 S no flip

WRAPS = {
    (1, N): (9, W, False),  # AB
    (1, W): (6, W, True),  # AD
    (2, N): (9, S, False),  # BC
    (2, E): (7, E, True),  # CF
    (6, N): (4, W, False),  # DG
    (2, S): (4, E, False),  # EF
    (7, S): (9, E, False),  # HC
}
WRAPS |= {(ti, te): (fi, fe, flip) for (fi, fe), (ti, te, flip) in WRAPS.items()}


def get_next(r, c, dir):
    face_id = (r // 50) * 3 + (c // 50)
    fr, fc = r % 50, c % 50
    on_edge = (
        (dir == L and fc == 0)
        or (dir == R and fc == 49)
        or (dir == U and fr == 0)
        or (dir == D and fr == 49)
    )
    if on_edge and (face_id, dir) in WRAPS:
        nface_id, nedge, flip = WRAPS[(face_id, dir)]
        offset = fr if dir in [L, R] else fc
        offset = 49 - offset if flip else offset
        nr, nc = 50 * (nface_id // 3), 50 * (nface_id % 3)
        if nedge in [W, E]:
            nr += offset
            if nedge == E:
                nc += 49
        elif nedge in [N, S]:
            nc += offset
            if nedge == S:
                nr += 49
        return nr, nc, (nedge - 2) % 4
    else:
        dr, dc = DIR[dir]
        return r + dr, c + dc, dir


with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

grid = [list(line) for line in lines[:-2]]
w = max(len(r) for r in grid)
grid = [list(line) + [" "] * (w - len(line)) for line in lines[:-2]]
moves = re.findall(r"(\d+|[LR])", lines[-1])

vgrid = grid.copy()

r, c = 0, 50
dir = R
for move in moves:
    if move in "LR":
        dir = (dir + (1 if move == "R" else -1)) % 4
    else:
        for _ in range(int(move)):
            vgrid[r][c] = DIRV[dir]
            nr, nc, ndir = get_next(r, c, dir)
            if grid[nr][nc] == "#":
                break
            r, c, dir = nr, nc, ndir

# for row in vgrid:
#     print(" ".join(row))

print((r + 1) * 1000 + (c + 1) * 4 + dir)  # 135297
