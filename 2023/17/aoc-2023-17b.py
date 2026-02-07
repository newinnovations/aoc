#!/usr/bin/env python3

import heapq

DIRS = [(1, 0, 1), (-1, 0, -1), (2, 1, 0), (-2, -1, 0)]
DIRV = "=>v^<"


# state: row, column, direction, direction_count
type state_type = tuple[int, int, int, int]


def generic_dijkstra(start, finish):
    start_r, start_c = start
    finish_r, finish_c = finish

    best_overall = float("inf")
    end_states = set()
    state: state_type = (start_r, start_c, 0, 0)
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state
    parents: dict[state_type, set[state_type]] = {state: set()}  # Parents

    while pq:
        cost, state = heapq.heappop(pq)

        # Generic end condition, also in case we want to find all best paths.
        # It ends when we encouter a state with worse cost than the goal.
        if cost > best_overall:
            break

        r, c, dir, dir_count = state

        # Dijkstra guard: skip states with worse cost than already found
        if best.get(state, float("inf")) < cost:
            continue

        # Goal check, in 17b we now must also check dir_count
        if (r, c) == (finish_r, finish_c) and dir_count > 3:
            best_overall = cost
            end_states.add(state)

            # break or continue: If we want only a single path we can stop now
            # otherwise continue reading the queue
            break

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
            if 0 <= nr < R and 0 <= nc < C:
                # (1) check if allowed, skip if not
                if dir and d != dir and dir_count < 4:
                    continue
                ndir_count = dir_count + 1 if d == dir else 1
                if ndir_count > 10 or d == -dir:
                    continue
                # (2) check against best already found for that next state
                ncost = cost + maze[nr][nc]
                nstate = (nr, nc, d, ndir_count)
                nbest = best.get(nstate, float("inf"))
                if ncost > nbest:  # worse
                    continue
                if ncost == nbest:  # equal: continue or process
                    continue
                    # parents[nstate].add(state)
                else:  # better
                    parents[nstate] = {state}
                    best[nstate] = ncost
                heapq.heappush(pq, (ncost, nstate))
    return best_overall, end_states, parents


with open(0) as f:
    maze = [list(map(int, list(line.strip()))) for line in f]
    R, C = len(maze), len(maze[0])

vmaze = [["."] * C for _ in range(R)]
best, end_states, parents = generic_dijkstra((0, 0), (R - 1, C - 1))

# Reconstruct single path by walking parents backwards
states = end_states
while states:
    state = states.pop()  # only consider one option
    r, c, dir, _ = state
    vmaze[r][c] = DIRV[dir]
    states = parents[state]

for row in vmaze:
    print(" ".join(row))

print(best)  # 1010
