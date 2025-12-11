#!/usr/bin/env python3


from collections import deque


def topological_sort(devices):  # Kahn's algorithm, graph must be DAG (no cycles)
    # Count indegrees based on edges present in the graph.
    indegrees = {node: 0 for node in devices}
    for node in devices:
        for edge in devices[node]:
            indegrees[edge] += 1

    # Queue with nodes with an indegree of 0 (initialy only "svr")
    queue = deque([node for node in devices if indegrees[node] == 0])

    order = []
    while queue:
        node = queue.popleft()  # Pick a node with indegree 0
        order.append(node)  # Output it
        for edge in devices[node]:  # Remove its outgoing edges
            indegrees[edge] -= 1
            if indegrees[edge] == 0:
                queue.append(edge)

    if len(order) != len(devices):  # Check graph was indeed DAG
        raise ValueError("Graph contains a cycle")

    return order


def bit_for(node):
    if node == "fft":
        return 1
    if node == "dac":
        return 2
    return 0


devices = dict()
with open("input.txt") as f:
    for line in f:
        s = line.strip().split(": ")
        devices[s[0]] = s[1].split(" ")
devices["out"] = []

# bottom-up approach similar to 2025:7

# cnt[node][mask] = number of paths from node to target with 'mask' nodes already seen
#
#   0b00 (0) — already seen none
#   0b01 (1) — already seen "fft"
#   0b10 (2) — already seen "dac"
#   0b11 (3) — already seen both

cnt = {node: [0, 0, 0, 0] for node in devices}
cnt["out"] = [0, 0, 0, 1]  # count 1 if seen both, otherwise 0

for node in reversed(topological_sort(devices)[:-1]):
    node_bit = bit_for(node)
    for m in range(4):
        mask = m | node_bit
        cnt[node][m] = sum(cnt[edge][mask] for edge in devices[node])

# number of paths from start when "fft" and "dac" not yet seen
print(cnt["svr"][0])  # 509312913844956
