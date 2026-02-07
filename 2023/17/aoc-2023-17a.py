#!/usr/bin/env python3

import heapq

DIRS = [(1, 0, 1), (-1, 0, -1), (2, 1, 0), (-2, -1, 0)]
DIRV = "=>v^<"

# state: row, column, direction, direction_count
type state_type = tuple[int, int, int, int]


def dijkstra(start, finish):
    start_r, start_c = start
    finish_r, finish_c = finish

    state: state_type = (start_r, start_c, 0, 0)
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state
    parent: dict[state_type, state_type | None] = {state: None}  # Parents

    while pq:
        cost, state = heapq.heappop(pq)

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

        for d, dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ncost = cost + maze[nr][nc]
                ndir_count = dir_count + 1 if d == dir else 1
                if ndir_count > 3 or d == -dir:
                    continue
                nstate = (nr, nc, d, ndir_count)
                if ncost < best.get(nstate, float("inf")):
                    best[nstate] = ncost
                    parent[nstate] = state
                    heapq.heappush(pq, (ncost, nstate))
    return 0, []


with open(0) as f:
    maze = [list(map(int, list(line.strip()))) for line in f]
    R, C = len(maze), len(maze[0])

vmaze = [["."] * C for _ in range(R)]
cost, path = dijkstra((0, 0), (R - 1, C - 1))
for r, c, d in path:
    vmaze[r][c] = DIRV[d]

for row in vmaze:
    print(" ".join(row))

print(cost)  # 866
