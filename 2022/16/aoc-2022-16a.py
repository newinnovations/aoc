#!/usr/bin/env python3

import re


def condense_graph(connections, broken_valves):
    conn = connections
    for broken_valve in broken_valves:
        rm_c = conn[broken_valve]  # remove this connection rm_c
        new_conn = {}
        for src, dest in conn.items():
            if src == broken_valve and src != "AA":
                continue
            new_dest = dest.copy()
            for dst, dist in dest.items():
                if dst == broken_valve:
                    del new_dest[dst]
                    for dst2, dist2 in rm_c.items():
                        if dst2 != src:
                            new_dest[dst2] = min(
                                dist + dist2, new_dest.get(dst2, float("inf"))
                            )
            new_conn[src] = new_dest
        conn = new_conn
    return conn


def part1(conn, rates, bits, N):
    def add(minute, loc, opened, released):
        if minute < N:
            nstate = (loc, opened)
            if state_max[minute].get(nstate, -1) < released:
                q[minute].add(nstate)
                state_max[minute][nstate] = released

    all_open = sum(bits.values())
    max_released = 0
    q = [set() for _ in range(N)]
    state_max = [dict() for _ in range(N)]

    add(0, "AA", 0, 0)
    for minute in range(30):
        for state in q[minute]:
            loc, opened = state
            released = state_max[minute][state]
            max_released = max(max_released, released)
            if opened != all_open:
                if loc != "AA" and not opened & bits[loc]:
                    add(
                        minute + 1,
                        loc,
                        opened | bits[loc],
                        released + (30 - (minute + 1)) * rates[loc],
                    )
                for c, d in conn[loc].items():
                    add(minute + d, c, opened, released)
    return max_released


conn = {}
broken_valves = []
rates = {}
pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
with open(0) as f:
    for line in f:
        f, rate, to = re.findall(pattern, line.strip())[0]
        rates[f] = int(rate)
        if rate == "0":
            broken_valves.append(f)
        conn[f] = {d: 1 for d in to.split(", ")}

conn = condense_graph(conn, broken_valves)
bits = {k: 1 << i for i, k in enumerate(conn) if k != "AA"}

print(part1(conn, rates, bits, 30))  # 1850
