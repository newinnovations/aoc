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


type state_type = tuple[str, frozenset]


def dijkstra(start, num_keys):
    state: state_type = (start, frozenset())
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state

    while pq:
        cost, state = heapq.heappop(pq)
        pos, keys = state

        # Dijkstra guard: skip states with worse cost than already found
        if best[state] < cost:
            continue

        # Goal check
        if len(keys) == num_keys:
            return cost

        for npos, dcost in conn[pos].items():
            # (1) check if allowed, skip if not
            if "A" <= npos <= "Z" and npos.lower() not in keys:
                continue
            # (2) check against best already found for that next state
            ncost = cost + dcost
            if "a" <= npos <= "z":
                nstate = (npos, keys.union([npos]))
            else:
                nstate = (npos, keys)
            nbest = best.get(nstate, float("inf"))
            if ncost < nbest:  # better
                best[nstate] = ncost
                heapq.heappush(pq, (ncost, nstate))


def find(target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    raise ValueError("failed to find target")


with open(0) as f:
    maze = [list(line.strip()) for line in f]
    nrows, ncols = len(maze), len(maze[0])

num_keys = sum("a" <= ch <= "z" for row in maze for ch in row)

conn = connections(maze)
print(dijkstra("@", num_keys))  # 5450
