#!/usr/bin/env python3

import heapq

N = 2
g_pos = [2, 4, 6, 8]
allowed = [0, 1, 3, 5, 7, 9, 10]
COST = [1, 10, 100, 1000]


def is_path_free(f, t, hallway):
    return all(hallway[i] == -1 for i in range(min(f, t), 1 + max(f, t)) if i != f)


def next_states(rooms, hallway, cost):
    states = []
    for r in range(4):
        if all(x == r for x in rooms[r]):  # includes empty room all([]) == True
            continue
        f = (r + 1) * 2
        steps = 1 + N - len(rooms[r])
        moving = rooms[r][0]
        nrooms = tuple(rooms[r1][1:] if r1 == r else rooms[r1] for r1 in range(4))
        for t in allowed:
            if is_path_free(f, t, hallway):
                nhw = tuple(moving if i == t else hallway[i] for i in range(11))
                ncost = cost + COST[moving] * (steps + abs(f - t))
                states.append((nrooms, nhw, ncost))
    for f in allowed:
        if (moving := hallway[f]) != -1 and all(x == moving for x in rooms[moving]):
            t = g_pos[moving]
            if is_path_free(f, t, hallway):
                steps = N - len(rooms[moving]) + abs(t - f)
                ncost = cost + COST[moving] * steps
                nrooms = tuple(
                    (r1,) + rooms[r1] if r1 == moving else rooms[r1] for r1 in range(4)
                )
                nhw = tuple(-1 if i == f else hallway[i] for i in range(11))
                states.append((nrooms, nhw, ncost))
    return states


type state_type = tuple[tuple, tuple]


def dijkstra(rooms, hallway, end):
    state: state_type = (rooms, hallway)
    pq: list[tuple[int, state_type]] = [(0, state)]  # Priority queue
    best: dict[state_type, int] = {state: 0}  # Best known cost for each state
    while pq:
        cost, state = heapq.heappop(pq)
        r, hw = state

        # Dijkstra guard: skip states with worse cost than already found
        if best[state] < cost:
            continue

        # Goal check
        if r == end:
            return cost

        for nr, nhw, ncost in next_states(r, hw, cost):
            nstate = (nr, nhw)
            nbest = best.get(nstate, float("inf"))
            if ncost >= nbest:  # worse or equal: skip
                continue
            best[nstate] = ncost
            heapq.heappush(pq, (ncost, nstate))
    raise ValueError("failed to solve")


total = 0
with open(0) as f:
    grid = [list(line.rstrip()) for line in f]

for row in grid:
    print(" ".join(row))

end = tuple([tuple([x] * N) for x in range(4)])
rooms = tuple(
    zip(*[["ABCD".find(ch) for ch in grid[r] if ch in "ABCD"] for r in range(2, 2 + N)])
)
hallway = tuple([-1 for _ in range(11)])

print(dijkstra(rooms, hallway, end))  # 19059
