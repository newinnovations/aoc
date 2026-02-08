#!/usr/bin/env python3

from collections import deque

type state_type = tuple[int, int]


def bfs(maze):
    rows, cols = len(maze), len(maze[0])

    visited: set[state_type] = set()
    parent: dict[state_type, state_type] = dict()
    state: state_type = (0, 0)

    q: deque[state_type] = deque([state])
    visited.add(state)

    while q:
        state = q.popleft()

        if state == (rows - 1, cols - 1):
            # Reconstruct path by walking parents backwards
            path = []
            while True:
                path.insert(0, state)
                if state not in parent:
                    break
                state = parent[state]
            return path

        r, c = state
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nstate = (nr, nc)
                if maze[nr][nc] == "." and nstate not in visited:
                    parent[nstate] = state
                    visited.add(nstate)
                    q.append(nstate)

    return None


size, num, filename = 70, 1024, "input.txt"
# size, num, filename = 6, 12, "ref.txt"

maze = [["."] * (size + 1) for _ in range(size + 1)]

with open(filename) as f:
    pos = [list(map(int, list(line.split(",")))) for line in f]

for x, y in pos[:num]:
    maze[y][x] = "#"

solution = bfs(maze)
if solution:
    for r, c in solution:
        maze[r][c] = "☢"
    print()
    for row in maze:
        print(" ".join(row))
    print()
    print(len(solution) - 1)  # 296
