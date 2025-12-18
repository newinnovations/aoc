#!/usr/bin/env python3

"""Try to solve maze.

Twist: you may break through the wall once to find shorter path.

Output how many cheats would save you at least 100 steps.
"""


from collections import defaultdict, deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find(target, maze):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return (r, c)
    raise ValueError(f"failed to find target '{target}'")


def bfs_one_cheat(maze, start):
    """Standard BFS on open cells only and one cheat. Returns 2D distances (=-1 if unreachable)."""
    rows, cols = len(maze), len(maze[0])
    sr, sc = start
    dist = [[-1] * cols for _ in range(rows)]
    dq = deque([(sr, sc)])
    dist[sr][sc] = 0
    while dq:
        r, c = dq.popleft()
        if maze[r][c] == "#":
            continue
        nd = dist[r][c] + 1
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows - 1 and 0 < nc < cols - 1:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = nd
                    dq.append((nr, nc))
    return dist


# def print_dist(dist):
#     for r in dist:
#         for c in r:
#             if c == -1:
#                 print("--", end=" ")
#             else:
#                 print(f"{c:2}", end=" ")
#         print()
#     print()


def count_save_100(maze):
    rows, cols = len(maze), len(maze[0])

    S = find("S", maze)
    E = find("E", maze)

    dsc = bfs_one_cheat(maze, S)  # dist from start
    dec = bfs_one_cheat(maze, E)  # dist to end

    closed_locs = [
        (r, c)
        for r, row in enumerate(maze)
        for c, ch in enumerate(row)
        if ch == "#" and 0 < r < rows - 1 and 0 < c < cols - 1
    ]

    hist = defaultdict(int)  # distance -> count of walls yielding that distance
    for r, c in closed_locs:
        dist_s = dsc[r][c]
        dist_e = dec[r][c]
        if dist_s != -1 and dist_e != -1:
            hist[dist_s + dist_e] += 1

    D0 = dsc[E[0]][E[1]]

    # print(D0)
    # for d in sorted(hist.keys()):
    #     improvement = D0 - d
    #     print(improvement, hist[d])

    save_100 = sum(count for d, count in hist.items() if (D0 - d) >= 100)
    print(save_100)


if __name__ == "__main__":
    maze = []
    with open("input.txt") as f:
        for line in f:
            maze.append(list(line.rstrip("\n")))
    count_save_100(maze)
