#!/usr/bin/env python3

import re
from collections import deque
from functools import cache
from itertools import combinations


def dist_graph(connections, rates):
    def dist(conn, src, dst):
        q = deque([(src, 0)])
        seen = set()
        while q:
            loc, d = q.popleft()
            if loc == dst:
                return d
            for loc2 in conn[loc]:
                nstate = (loc2, d + 1)
                if nstate not in seen:
                    seen.add(nstate)
                    q.append(nstate)
        raise ValueError("dest not found")

    connd = {}
    for a, b in combinations(rates, 2):
        d = dist(connections, a, b)
        if b != "AA":
            connd.setdefault(a, {})[b] = d
        if a != "AA":
            connd.setdefault(b, {})[a] = d
    return connd


def part1(N, dgraph, rates, bits):
    max_released = 0
    seen = set()
    q = deque([(N, "AA", 0, 0)])
    while q:
        t, loc, opened, released = q.popleft()
        max_released = max(max_released, released)
        for nloc, dist in dgraph[loc].items():
            nt = t - dist - 1
            if nt > 0 and not (opened & bits[nloc]):
                nstate = (
                    nt,
                    nloc,
                    opened | bits[nloc],
                    released + nt * rates[nloc],
                )
                if nstate not in seen:
                    seen.add(nstate)
                    q.append(nstate)
    return max_released


def part1_dfs(N, dgraph, rates, bits):
    @cache
    def max_released_dfs(t, loc, opened):
        max_rel = 0
        for nloc, dist in dgraph[loc].items():
            nt = t - dist - 1
            if nt > 0 and not opened & bits[nloc]:
                released = nt * rates[nloc] + max_released_dfs(
                    nt, nloc, opened | bits[nloc]
                )
                max_rel = max(max_rel, released)
        return max_rel

    return max_released_dfs(N, "AA", 0)


def part2(N, dgraph, rates, bits):
    def add(t1, loc1, t2, loc2, opened, released):
        if loc1 < loc2:
            state = (t1, loc1, t2, loc2, opened)
        else:
            state = (t2, loc2, t1, loc1, opened)
        if seen.get(state, -1) < released:
            seen[state] = released
            q.append(state)

    max_released = 0
    state = (N, "AA", N, "AA", 0)
    q = deque([state])
    seen = {state: 0}
    while q:
        state = q.popleft()
        t1, loc1, t2, loc2, opened = state  # t = remaining
        released = seen[state]
        max_released = max(max_released, released)

        next1 = [
            (loc, t1 - dist - 1)
            for loc, dist in dgraph[loc1].items()
            if (not (opened & bits[loc])) and (t1 - dist - 1 > 0)
        ]
        next2 = [
            (loc, t2 - dist - 1)
            for loc, dist in dgraph[loc2].items()
            if (not (opened & bits[loc])) and (t2 - dist - 1 > 0)
        ]

        if len(next1) == 1 and len(next2) == 1:
            (nloc1, nt1), (nloc2, nt2) = next1[0], next2[0]
            if nloc1 == nloc2:
                if nt2 > nt1:
                    next1 = []
                else:
                    next2 = []

        if next1 and next2:
            for nloc1, nt1 in next1:
                nopened1 = opened | bits[nloc1]
                nreleased1 = released + nt1 * rates[nloc1]
                for nloc2, nt2 in next2:
                    if nloc1 != nloc2:
                        add(
                            nt1,
                            nloc1,
                            nt2,
                            nloc2,
                            nopened1 | bits[nloc2],
                            nreleased1 + nt2 * rates[nloc2],
                        )

        if next1 and not next2:
            for nloc1, nt1 in next1:
                add(
                    nt1,
                    nloc1,
                    t2,
                    loc2,
                    opened | bits[nloc1],
                    released + nt1 * rates[nloc1],
                )

        if next2 and not next1:
            for nloc2, nt2 in next2:
                add(
                    t1,
                    loc1,
                    nt2,
                    nloc2,
                    opened | bits[nloc2],
                    released + nt2 * rates[nloc2],
                )

    return max_released


def part2_dfs(N, dgraph, rates, bits):
    def get_max(t1, loc1, t2, loc2, opened, released):
        if loc2 < loc1:
            return released + max_released_dfs(t2, loc2, t1, loc1, opened)
        else:
            return released + max_released_dfs(t1, loc1, t2, loc2, opened)

    @cache
    def max_released_dfs(t1, loc1, t2, loc2, opened):
        max_rel = 0

        next1 = [
            (loc, t1 - dist - 1)
            for loc, dist in dgraph[loc1].items()
            if (not (opened & bits[loc])) and (t1 - dist - 1 > 0)
        ]
        next2 = [
            (loc, t2 - dist - 1)
            for loc, dist in dgraph[loc2].items()
            if (not (opened & bits[loc])) and (t2 - dist - 1 > 0)
        ]

        if len(next1) == 1 and len(next2) == 1:
            (nloc1, nt1), (nloc2, nt2) = next1[0], next2[0]
            if nloc1 == nloc2:
                if nt2 > nt1:
                    next1 = []
                else:
                    next2 = []

        if next1 and next2:
            for nloc1, nt1 in next1:
                nopened1 = opened | bits[nloc1]
                nreleased1 = nt1 * rates[nloc1]
                for nloc2, nt2 in next2:
                    if nloc1 != nloc2:
                        max_rel = max(
                            max_rel,
                            get_max(
                                nt1,
                                nloc1,
                                nt2,
                                nloc2,
                                nopened1 | bits[nloc2],
                                nreleased1 + nt2 * rates[nloc2],
                            ),
                        )

        if next1 and not next2:
            for nloc1, nt1 in next1:
                max_rel = max(
                    max_rel,
                    get_max(
                        nt1,
                        nloc1,
                        t2,
                        loc2,
                        opened | bits[nloc1],
                        nt1 * rates[nloc1],
                    ),
                )

        if next2 and not next1:
            for nloc2, nt2 in next2:
                max_rel = max(
                    max_rel,
                    get_max(
                        t1,
                        loc1,
                        nt2,
                        nloc2,
                        opened | bits[nloc2],
                        nt2 * rates[nloc2],
                    ),
                )

        return max_rel

    return max_released_dfs(N, "AA", N, "AA", 0)


conn, rates = {}, {}
pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
with open(0) as f:
    for line in f:
        f, rate, to = re.findall(pattern, line.strip())[0]
        if rate != "0" or f == "AA":
            rates[f] = int(rate)
        conn[f] = to.split(", ")
bits = {k: 1 << i for i, k in enumerate(rates) if k != "AA"}
dgraph = dist_graph(conn, rates)

# print(part1(30, dgraph, rates, bits))  # 1850 (0.3 sec)
# print(part1_dfs(30, dgraph, rates, bits))  # 1850 (0.1 sec)
# print(part2(26, dgraph, rates, bits))  # 2306 (42 sec)
print(part2_dfs(26, dgraph, rates, bits))  # 2306 (28 sec)
