#!/usr/bin/env python3

# 4-directional moves
DIRS = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}


maze = list()
with open("ref.txt") as f:
    for line in f:
        maze.append(list(line.strip()))


def longest_path(maze, start, end):
    """
    Find the length of the longest simple path (no revisits) between start and end in a grid maze.
    # = wall, . = normal path, v^<> = path with required direction
    """

    R = len(maze)
    C = len(maze[0]) if R else 0

    sr, sc = start
    er, ec = end

    best_path = []
    visited = [[False] * C for _ in range(R)]

    def dfs(r, c, path):
        nonlocal best_path

        # If we reached end, update best path
        if (r, c) == (er, ec):
            if len(path) > len(best_path):
                best_path = path.copy()

        if maze[r][c] == ".":
            dirs = DIRS.values()
        else:
            dirs = [DIRS[maze[r][c]]]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < R
                and 0 <= nc < C
                and maze[nr][nc] != "#"
                and not visited[nr][nc]
            ):
                visited[nr][nc] = True
                path.append((nr, nc))
                dfs(nr, nc, path)
                path.pop()
                visited[nr][nc] = False

    visited[sr][sc] = True
    dfs(sr, sc, [(sr, sc)])

    length_in_steps = max(0, len(best_path) - 1)
    return length_in_steps, best_path


start = (0, 1)
end = (len(maze) - 1, len(maze[0]) - 2)
length, _ = longest_path(maze, start, end)
print(length)
