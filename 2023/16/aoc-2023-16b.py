#!/usr/bin/env python3

from collections import deque

R, L, D, U = 1, -1, 2, -2
DIRS = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRV = "=>v^<"

type state_type = tuple[int, int, int]


def continue_ray(q, r, c, dir):
    dr, dc = DIRS[dir]
    q.append((r + dr, c + dc, dir))


def split_ray(q, r, c, dir):
    rot = 1 if abs(dir) == 2 else 2
    dr, dc = DIRS[rot]
    q.append((r + dr, c + dc, rot))
    dr, dc = DIRS[-rot]
    q.append((r + dr, c + dc, -rot))


with open("input.txt") as f:
    maze = [list(line.strip()) for line in f]
    ROWS, COLS = len(maze), len(maze[0])


def num_energized(r, c, dir):
    visited: set[state_type] = set()
    state: state_type = (r, c, dir)  # r, c, dir
    q: deque[state_type] = deque([state])
    while q:
        state = q.popleft()
        if state in visited:
            continue
        r, c, dir = state
        if 0 <= r < ROWS and 0 <= c < COLS:
            visited.add(state)
            match maze[r][c]:
                case "|":
                    if abs(dir) == 2:
                        continue_ray(q, r, c, dir)
                    else:
                        split_ray(q, r, c, dir)
                case "-":
                    if abs(dir) == 1:
                        continue_ray(q, r, c, dir)
                    else:
                        split_ray(q, r, c, dir)
                case "\\":
                    if dir == R:
                        continue_ray(q, r, c, D)
                    elif dir == D:
                        continue_ray(q, r, c, R)
                    elif dir == L:
                        continue_ray(q, r, c, U)
                    elif dir == U:
                        continue_ray(q, r, c, L)
                case "/":
                    if dir == R:
                        continue_ray(q, r, c, U)
                    elif dir == U:
                        continue_ray(q, r, c, R)
                    elif dir == L:
                        continue_ray(q, r, c, D)
                    elif dir == D:
                        continue_ray(q, r, c, L)
                case ".":
                    continue_ray(q, r, c, dir)
                case _:
                    raise ValueError("Unknown maze char")

    return len({(r, c) for r, c, _ in visited})


max_energized = 0

for r in range(ROWS):
    n = num_energized(r, 0, R)
    if n > max_energized:
        max_energized = n
    n = num_energized(r, COLS - 1, L)
    if n > max_energized:
        max_energized = n

for c in range(COLS):
    n = num_energized(0, c, D)
    if n > max_energized:
        max_energized = n
    n = num_energized(ROWS - 1, c, U)
    if n > max_energized:
        max_energized = n

print(max_energized)  # 8143
