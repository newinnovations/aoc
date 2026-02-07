#!/usr/bin/env python3

import heapq
from collections import deque


def connections(maze):
    conn = dict()
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch != "#" and ch != ".":
                res = dict()
                seen = set()
                q = deque([(0, (r, c))])
                while q:
                    cost, (ri, ci) = q.popleft()
                    if maze[ri][ci] not in [".", ch]:
                        res[maze[ri][ci]] = cost
                    else:
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = ri + dr, ci + dc
                            if maze[nr][nc] != "#" and (nr, nc) not in seen:
                                q.append((cost + 1, (nr, nc)))
                                seen.add((nr, nc))
                conn[ch] = res
    return conn


type state_type = tuple[frozenset, frozenset]


def generic_dijkstra2(start, nkeys):
    state: state_type = (start, frozenset())
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state

    while pq:
        cost, state = heapq.heappop(pq)
        pos4, keys = state

        # print(cost, state)

        # Dijkstra guard: skip states with worse cost than already found
        if best[state] < cost:
            continue

        # Goal check
        if len(keys) == nkeys:
            return cost

        for pos in pos4:
            for npos1, dcost in conn[pos].items():
                # (1) check if allowed, skip if not
                if "A" <= npos1 <= "Z" and npos1.lower() not in keys:
                    continue
                # (2) check against best already found for that next state
                ncost = cost + dcost
                npos4 = pos4.difference([pos]).union([npos1])
                if "a" <= npos1 <= "z":
                    nstate4 = (npos4, keys.union([npos1]))
                else:
                    nstate4 = (npos4, keys)
                assert len(npos4) == 4
                nbest = best.get(nstate4, float("inf"))
                if ncost < nbest:  # better
                    best[nstate4] = ncost
                    heapq.heappush(pq, (ncost, nstate4))


def find(target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    raise ValueError("failed to find target")


with open(0) as f:
    maze = [list(line.strip()) for line in f]
    nrows, ncols = len(maze), len(maze[0])

KEYS = set()
for row in maze:
    for ch in row:
        if "a" <= ch <= "z":
            KEYS.add(ch)
nkeys = len(KEYS)

r, c = find("@")
maze[r][c] = "#"
maze[r - 1][c] = "#"
maze[r + 1][c] = "#"
maze[r][c - 1] = "#"
maze[r][c + 1] = "#"
maze[r - 1][c - 1] = "1"
maze[r - 1][c + 1] = "2"
maze[r + 1][c - 1] = "3"
maze[r + 1][c + 1] = "4"

conn = connections(maze)
for k, v in conn.items():
    print(k, v)

print(generic_dijkstra2(frozenset(["1", "2", "3", "4"]), nkeys))  # 2020
