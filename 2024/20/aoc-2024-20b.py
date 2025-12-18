#!/usr/bin/env python3

from collections import defaultdict, deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find(target, maze):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return (r, c)
    raise ValueError(f"failed to find target '{target}'")


def distances(maze, start):
    """Standard BFS on open cells only. Returns distances (-1 if unreachable)."""
    rows, cols = len(maze), len(maze[0])
    sr, sc = start
    dist = [[-1] * cols for _ in range(rows)]
    dq = deque([(sr, sc)])
    dist[sr][sc] = 0
    while dq:
        r, c = dq.popleft()
        nd = dist[r][c] + 1
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows - 1 and 0 < nc < cols - 1:
                if maze[nr][nc] != "#" and dist[nr][nc] == -1:
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


def count_save_100(maze, K):
    S = find("S", maze)
    E = find("E", maze)

    ds = distances(maze, S)  # dist from start
    de = distances(maze, E)  # dist to end

    open_locs = [
        (r, c) for r, row in enumerate(maze) for c, ch in enumerate(row) if ch != "#"
    ]

    hist = defaultdict(int)  # distance -> count of paths yielding that distance
    for sr, sc in open_locs:
        for er, ec in open_locs:
            dist = abs(sr - er) + abs(sc - ec)
            if dist == 0 or dist > K:
                continue
            dist_s = ds[sr][sc]
            dist_e = de[er][ec]
            if dist_s != -1 and dist_e != -1:
                hist[dist_s + dist + dist_e] += 1

    D0 = ds[E[0]][E[1]]

    # print(D0)
    # for d in sorted(hist.keys()):
    #     improvement = D0 - d
    #     if improvement >= 50:
    #         print(improvement, hist[d])

    save_100 = sum(count for d, count in hist.items() if (D0 - d) >= 100)
    print(save_100)


if __name__ == "__main__":
    with open("input.txt") as f:
        maze = [list(line.rstrip("\n")) for line in f]
    count_save_100(maze, 20)
