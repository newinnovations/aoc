#!/usr/bin/env python3

import heapq
from collections import deque

R, L, D, U = 1, -1, 2, -2
DIR = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRV = "=>v^<"
DIRS = [(d, dr, dc) for d, (dr, dc) in DIR.items()]  # speedup

SHOW_MAZE = True

# state: row, column, direction
type state_type = tuple[int, int, int]


def generic_dijkstra(start, finish):
    start_r, start_c = start
    finish_r, finish_c = finish

    best_overall = float("inf")
    end_states = set()
    state: state_type = (start_r, start_c, 1)
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state
    parents: dict[state_type, set[state_type]] = {state: set()}  # Parents

    while pq:
        cost, state = heapq.heappop(pq)

        # Generic end condition, also in case we want to find all best paths.
        # It ends when we encouter a state with worse cost than the goal.
        if cost > best_overall:
            break

        r, c, dir = state

        # Dijkstra guard: skip states with worse cost than already found
        if best[state] < cost:
            continue

        # Goal check
        if (r, c) == (finish_r, finish_c):
            best_overall = cost
            end_states.add(state)
            # break or continue: If we want only a single path we can stop now
            # otherwise continue processing the queue
            continue

        # Look at all possible next states
        # (1) check if allowed, skip if not
        # (2) check against best already found for that next state
        #    worse: skip
        #    equal: this is another best path. Only add this next state to the queue
        #           if we want to find all the best paths. In that case add the parent
        #           to the list of parents for this state.
        #   better: reset the set of parents for this next state to only this one as
        #           the existing parents in the set are for worse paths. Update best
        #           known cost for this next state.
        for d, dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                # (1) check if allowed, skip if not
                if maze[nr][nc] == "#" or d == -dir:
                    continue
                # (2) check against best already found for that next state
                ncost = cost + 1 if d == dir else cost + 1001
                nstate = (nr, nc, d)
                nbest = best.get(nstate, float("inf"))
                if ncost > nbest:  # worse: skip
                    continue
                if ncost == nbest:  # equal: in 16b we process
                    parents[nstate].add(state)
                else:  # better
                    parents[nstate] = {state}
                    best[nstate] = ncost
                heapq.heappush(pq, (ncost, nstate))
    return best_overall, end_states, parents


def find(target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    raise ValueError("failed to find target")


with open("input.txt") as f:
    maze = [list(line.strip()) for line in f]
    nrows, ncols = len(maze), len(maze[0])


best, end_states, parents = generic_dijkstra(find("S"), find("E"))

# Reconstruct paths by walking parents backwards.
visited = set()
q = deque(end_states)
while q:
    state = q.popleft()
    r, c, _ = state
    visited.add((r, c))
    q.extend(parents[state])

if SHOW_MAZE:
    vmaze = [["."] * ncols for _ in range(nrows)]
    for r, c in visited:
        vmaze[r][c] = "O"
    for row in vmaze:
        print(" ".join(row))

print(len(visited))  # 496
