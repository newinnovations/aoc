#!/usr/bin/env python3

import heapq

# state: row, column
type state_type = tuple[int, int]


def dijkstra(start, finish):
    start_r, start_c = start
    finish_r, finish_c = finish

    state: state_type = (start_r, start_c)
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state

    while pq:
        cost, state = heapq.heappop(pq)
        r, c = state
        if (r, c) == (finish_r, finish_c):
            return cost
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                ncost = cost + grid[nr][nc]
                nstate = (nr, nc)
                if ncost < best.get(nstate, float("inf")):
                    best[nstate] = ncost
                    heapq.heappush(pq, (ncost, nstate))


total = 0
with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]
    nrows, ncols = len(grid), len(grid[0])

# for row in grid:
#     for c in row:
#         print(c, end=" ")
#     print()

print(dijkstra((0, 0), (nrows - 1, ncols - 1)))  # 315
