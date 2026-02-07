#!/usr/bin/env python3
from collections import deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_maze(filename):
    maze = []
    with open(filename) as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


def contract_maze(maze, start, end):
    """
    Contract corridors (degree-2 nodes) into edges between junctions.
    Returns: graph dict, junction_distances dict
    """
    R, C = len(maze), len(maze[0]) if maze else 0

    # Find all junctions (degree != 2) and special points
    junctions = set()
    junctions.add(start)
    junctions.add(end)

    for r in range(R):
        for c in range(C):
            if maze[r][c] == "#":
                continue
            neighbors = []
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != "#":
                    neighbors.append((nr, nc))
            # Junction if degree != 2 (or start/end)
            if len(neighbors) != 2:
                junctions.add((r, c))

    # Build contracted graph
    graph = {j: {} for j in junctions}

    for junction in junctions:
        # BFS from each junction to find adjacent junctions
        visited = {junction}
        queue = deque([(junction, 0)])

        while queue:
            (r, c), dist = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and maze[nr][nc] != "#"
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    new_dist = dist + 1

                    if (nr, nc) in junctions:
                        # Found adjacent junction
                        graph[junction][(nr, nc)] = new_dist
                    else:
                        # Continue through corridor
                        queue.append(((nr, nc), new_dist))

    return graph


def longest_path_contracted(graph, start, end):
    """
    Find longest path in contracted graph using iterative DFS.
    """
    visited = {start}
    stack = [(start, 0, iter(graph[start].items()))]
    best = 0

    while stack:
        node, dist, neighbors_iter = stack[-1]

        if node == end:
            best = max(best, dist)
            # Backtrack
            stack.pop()
            visited.remove(node)
            continue

        # Try next neighbor
        try:
            next_node, edge_dist = next(neighbors_iter)
            if next_node not in visited:
                visited.add(next_node)
                stack.append(
                    (next_node, dist + edge_dist, iter(graph[next_node].items()))
                )
        except StopIteration:
            # No more neighbors, backtrack
            stack.pop()
            visited.remove(node)

    return best


def longest_path_optimized(maze, start, end):
    """
    Optimized longest path with multiple strategies:
    1. Contract corridors into single edges
    2. Iterative DFS on contracted graph
    3. Early termination checks
    """
    R = len(maze)
    C = len(maze[0]) if R else 0

    if R == 0 or C == 0:
        return 0
    if maze[start[0]][start[1]] == "#":
        return 0

    # Contract the maze
    graph = contract_maze(maze, start, end)

    # If start and end are directly connected in contracted graph
    if end in graph[start]:
        # Still need to check for longer paths
        pass

    # Run DFS on contracted graph
    return longest_path_contracted(graph, start, end)


maze = read_maze(0)
start = (0, 1)
end = (len(maze) - 1, len(maze[0]) - 2)

length = longest_path_optimized(maze, start, end)
print(length)  # 6258
