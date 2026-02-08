#!/usr/bin/env python3

from collections import deque

type state_type = tuple[int, int]


def bfs(maze):
    rows, cols = len(maze), len(maze[0])

    visited: set[state_type] = set()
    state: state_type = (0, 0)

    q: deque[state_type] = deque([state])
    visited.add(state)

    while q:
        state = q.popleft()

        if state == (rows - 1, cols - 1):
            return True

        r, c = state
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nstate = (nr, nc)
                if maze[nr][nc] == "." and nstate not in visited:
                    visited.add(nstate)
                    q.append(nstate)

    return False


size, num, filename = 70, 1024, "input.txt"
# size, num, filename = 6, 12, "ref.txt"

maze = [["."] * (size + 1) for _ in range(size + 1)]

with open(filename) as f:
    pos = [list(map(int, list(line.split(",")))) for line in f]

for n, (x, y) in enumerate(pos):
    maze[y][x] = "#"
    if n >= num:
        solution = bfs(maze)
        if not solution:
            print(f"{x},{y}")  # 28,44
            break
