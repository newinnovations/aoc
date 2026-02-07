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


type state_type = tuple[tuple[tuple[str, int], ...], frozenset]
type q_state_type = tuple[str, frozenset]


def dijkstra(start, num_keys):
    state: state_type = (tuple((pos, 0) for pos in start), frozenset())
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    q_best: dict[q_state_type, int] = {(pos, frozenset()): 0 for pos in start}

    while pq:
        cost, state = heapq.heappop(pq)
        pos4, keys = state

        # Goal check
        if len(keys) == num_keys:
            return cost

        for i, (q_pos, q_cost) in enumerate(pos4):
            for n_q_pos, dcost in conn[q_pos].items():
                # (1) check if allowed, skip if not
                if "A" <= n_q_pos <= "Z" and n_q_pos.lower() not in keys:
                    continue
                # (2) check against best already found for that next state
                if "a" <= n_q_pos <= "z":
                    nkeys = keys.union([n_q_pos])
                else:
                    nkeys = keys
                n_q_state = (n_q_pos, nkeys)
                n_q_cost = q_cost + dcost
                qbest = q_best.get(n_q_state, float("inf"))
                if n_q_cost >= qbest:
                    continue
                n_q_pos4 = tuple(
                    (n_q_pos, n_q_cost) if i == j else p for j, p in enumerate(pos4)
                )
                for p, c in n_q_pos4:
                    n_q_state = (p, nkeys)
                    qbest = q_best.get(n_q_state, float("inf"))
                    if c < qbest:
                        q_best[n_q_state] = c
                ncost = cost + dcost
                nstate4 = (n_q_pos4, nkeys)
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

num_keys = sum("a" <= ch <= "z" for row in maze for ch in row)

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
print(dijkstra(["1", "2", "3", "4"], num_keys))  # 2020
