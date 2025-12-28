#!/usr/bin/env python3

import heapq

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
D180 = {"^": "v", "v": "^", "<": ">", ">": "<"}

type state_type = tuple[int, int, str, int]


def dijkstra():
    state: state_type = (start_r, start_c, "=", 0)
    q: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state
    parent: dict[state_type, state_type | None] = {state: None}  # Parents

    while q:
        cost, state = heapq.heappop(q)

        r, c, dir, dir_count = state

        # Dijkstra guard: skip outdated entries
        if best.get(state, float("inf")) < cost:
            continue

        # Goal check
        if (r, c) == (finish_r, finish_c):
            # Reconstruct path by walking parents backwards
            path = []
            while True:
                r, c, dir, _ = state
                path.append((r, c, dir))
                ps = parent[state]
                if ps is None:
                    break
                state = ps
            path.reverse()
            return cost, path

        for d, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ncost = cost + maze[nr][nc]
                ndir_count = dir_count + 1 if d == dir else 1
                if ndir_count > 3 or D180[d] == dir:
                    continue
                nstate = (nr, nc, d, ndir_count)
                if ncost < best.get(nstate, float("inf")):
                    best[nstate] = ncost
                    parent[nstate] = state
                    heapq.heappush(q, (ncost, nstate))
    return 0, []


maze = []
with open("input.txt") as f:
    for line in f:
        maze.append(list(map(int, list(line.strip()))))
R = len(maze)
C = len(maze[0])
start_r, start_c = (0, 0)
finish_r, finish_c = (R - 1, C - 1)

vmaze = [["."] * C for _ in range(R)]
cost, path = dijkstra()
for r, c, d in path:
    vmaze[r][c] = d

for row in vmaze:
    print(" ".join(row))

print(cost)
