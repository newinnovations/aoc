#!/usr/bin/env python3

"""
Just for fun: really try to fit the presents

Sample data

  Region 1: 4x4 with counts [0, 0, 0, 0, 2, 0]: fits YES

  A A A .
  A B B B
  A A A B
  . B B B

  Region 2: 12x5 with counts [1, 0, 1, 0, 2, 2]: fits YES

  . A A B B B . . D D D .
  A A A . B C C C D F F F
  A A E B B B C . D D D F
  . . E E E C C C . F F F
  . . E E E . . . . . . .

  Region 3: 12x5 with counts [1, 0, 1, 0, 3, 2]: fits NO

  Total: 2

Puzzle data (12m16s on Dell Latitude 5440, i7-1355U, 40GB RAM)

  Region 1: 50x50 with counts [46, 40, 42, 34, 52, 41]: fits YES
  Region 2: 45x49 with counts [37, 37, 51, 45, 32, 38]: fits YES
  Region 3: 46x44 with counts [54, 42, 59, 43, 65, 50]: fits NO
  Region 4: 37x47 with counts [50, 45, 48, 37, 42, 46]: fits NO
  Region 5: 41x46 with counts [29, 32, 34, 31, 29, 39]: fits YES
  ...
  Region 997: 35x39 with counts [21, 27, 24, 18, 31, 22]: fits YES
  Region 998: 45x38 with counts [33, 28, 26, 27, 31, 35]: fits YES
  Region 999: 40x46 with counts [45, 46, 46, 46, 57, 44]: fits NO
  Region 1000: 35x50 with counts [49, 57, 54, 38, 36, 30]: fits NO

  Total: 526
"""

FILENAME, SHOW_SOLUTION = "ref.txt", True
FILENAME, SHOW_SOLUTION = "input.txt", False


def rotate90(shape):
    return [list(row) for row in zip(*shape[::-1])]


def orientations(shape):
    res = [shape]
    for _ in range(3):
        shape = rotate90(shape)
        res.append(shape)
    return res


def shape_area(shape):
    return sum(1 for row in shape for c in row if c == "#")


def shape_offsets(shape):
    h = len(shape)
    w = len(shape[0])
    offs = [(r, c) for r in range(h) for c in range(w) if shape[r][c] == "#"]
    return offs, h, w


def render_board_labels(w, h, placements):
    board = [list("." * w) for _ in range(h)]
    for label, _, offs, tx, ty in placements:
        for dy, dx in offs:
            board[ty + dy][tx + dx] = label
    return [" ".join(row) for row in board]


def precompute_placements(w, h):
    """Precompute all legal placement masks (orientation+position) for each shape index."""
    placements_by_idx = {}

    def mask_from_offsets(tx, ty, offs):
        m = 0
        for dy, dx in offs:
            idx = (ty + dy) * w + (tx + dx)
            m |= 1 << idx
        return m

    for i, base in enumerate(shapes):
        plist = []
        for o in orientations(base):
            offs, rh, rw = shape_offsets(o)
            for ty in range(h - rh + 1):
                for tx in range(w - rw + 1):
                    m = mask_from_offsets(tx, ty, offs)
                    plist.append((m, offs, tx, ty))
        # dedup identical masks (symmetric orientations can collide)
        seen = set()
        uniq = []
        for m, offs, tx, ty in plist:
            if m not in seen:
                seen.add(m)
                uniq.append((m, offs, tx, ty))
        placements_by_idx[i] = uniq

    return placements_by_idx


def can_all_fit(w, h, present_counts):
    """Minimum-Remaining-Values (MRV) per piece, bitset mask, memoization"""
    total_needed = sum(shape_area(shapes[i]) * c for i, c in enumerate(present_counts))
    if total_needed > w * h:
        return False, []

    placements_by_idx = precompute_placements(w, h)
    areas = {i: shape_area(shapes[i]) for i in range(len(shapes))}

    counts = present_counts[:]
    total_to_place = sum(counts)
    memo = {}
    placement_stack = []

    def backtrack(placed, mask):
        if placed == total_to_place:
            return True

        key = (mask, tuple(counts))
        if key in memo:
            return False

        # Build feasible placements per remaining shape
        candidates_per_shape = []
        for i in range(len(counts)):
            if counts[i] == 0:
                continue
            feasible = [
                (m, offs, tx, ty)
                for (m, offs, tx, ty) in placements_by_idx[i]
                if (m & mask) == 0
            ]
            if not feasible:
                memo[key] = False
                return False
            candidates_per_shape.append((i, feasible))

        # MRV: choose shape with fewest feasible placements; tie-break by larger area
        candidates_per_shape.sort(key=lambda t: (len(t[1]), -areas[t[0]]))
        shape_idx, feasible_list = candidates_per_shape[0]

        label = chr(ord("A") + placed) if placed < 25 else "*"
        for m, offs, tx, ty in feasible_list:
            counts[shape_idx] -= 1
            placement_stack.append((label, shape_idx, offs, tx, ty))
            if backtrack(placed + 1, mask | m):
                return True
            placement_stack.pop()
            counts[shape_idx] += 1

        memo[key] = False
        return False

    if not backtrack(0, 0):
        return False, []

    if SHOW_SOLUTION:
        board_lines = render_board_labels(w, h, placement_stack)
        return True, board_lines
    else:
        return True, []


idx = -1
shapes_dict = dict()
presents = list()
with open(FILENAME) as f:
    for line in f:
        line = line.strip()
        if line.endswith(":"):
            idx = int(line[:-1])
            shapes_dict[idx] = list()
        elif "." in line or "#" in line:
            shapes_dict[idx].append(list(line))
        elif ":" in line:
            s = line.split(": ")
            width, height = map(int, s[0].split("x"))
            present_counts = list(map(int, s[1].split(" ")))
            presents.append((width, height, present_counts))

shapes = [shapes_dict[i] for i in range(len(shapes_dict.keys()))]

total = 0
for region_idx, (w, h, counts) in enumerate(presents, start=1):
    ok, board_lines = can_all_fit(w, h, counts)
    print(f"Region {region_idx}: {w}x{h} with counts {counts}: fits ", end="")
    if ok:
        print("YES")
        total += 1
        if SHOW_SOLUTION:
            print()
            for line in board_lines:
                print(line)
            print()
    else:
        print("NO")

print("\nTotal:", total)
