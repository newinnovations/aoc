#!/usr/bin/env python3

# 4-directional moves
DIRS = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

# Read maze
maze = []
with open(0) as f:
    for line in f:
        maze.append(list(line.strip()))


def longest_path_length(maze, start, end):
    """
    Iterative DFS (no recursion): length of the longest simple path (no revisits).
    '#' = wall, '.' = normal path, v^<> = path with required direction (outgoing).
    Returns number of steps (edges).
    """
    R = len(maze)
    C = len(maze[0]) if R else 0
    sr, sc = start
    er, ec = end

    if R == 0 or C == 0:
        return 0
    if maze[sr][sc] == "#":
        return 0

    # Precompute potential neighbors for each cell (ignores 'visited'; we handle that during traversal)
    neighbors = [[[] for _ in range(C)] for __ in range(R)]
    for r in range(R):
        for c in range(C):
            if maze[r][c] == "#":
                continue
            ch = maze[r][c]
            dirs = DIRS.values() if ch == "." else ([DIRS[ch]] if ch in DIRS else [])
            lst = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != "#":
                    lst.append((nr, nc))
            neighbors[r][c] = lst

    visited = [[False] * C for _ in range(R)]
    visited[sr][sc] = True

    # Stack holds frames: (row, col, next_child_index)
    stack = [(sr, sc, 0)]
    best = 0  # best length in steps (edges), i.e., len(stack) - 1 when at 'end'

    while stack:
        r, c, i = stack[-1]

        # If we're at the end, update best (edges = nodes_on_stack - 1)
        if (r, c) == (er, ec):
            if len(stack) - 1 > best:
                best = len(stack) - 1
            # Do not return; continue exploring other branches

        # If we've tried all children, backtrack
        if i >= len(neighbors[r][c]):
            stack.pop()
            visited[r][c] = False
            if stack:
                pr, pc, pi = stack[-1]
                stack[-1] = (pr, pc, pi + 1)  # advance parent's next_child_index
            continue

        # Otherwise, consider the i-th neighbor
        nr, nc = neighbors[r][c][i]
        if not visited[nr][nc]:
            visited[nr][nc] = True
            stack.append((nr, nc, 0))
        else:
            # Skip visited neighbor; advance to next
            stack[-1] = (r, c, i + 1)

    return best


start = (0, 1)
end = (len(maze) - 1, len(maze[0]) - 2)
length = longest_path_length(maze, start, end)
print(length)  # 2190
