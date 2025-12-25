#!/usr/bin/env python3

from functools import cache

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_maze(filename):
    maze = []
    with open(filename) as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


@cache
def neighbors(idx):
    r = idx // C
    c = idx % C
    lst = []
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != "#":
            lst.append(nr * C + nc)
    return lst


def find_start():
    for r_num, r in enumerate(maze):
        if "S" in r:
            c_num = r.index("S")
            return r_num * C + c_num
    return 0


def print_maze(pos_set):
    i = 0
    for r_num, r in enumerate(maze):
        for c_num, c in enumerate(r):
            if i in pos_set:
                print("O", end=" ")
            else:
                print(c, end=" ")
            i += 1
        print()
    print()


def do_step(pos_set):
    next = set()
    for i in pos_set:
        next.update(neighbors(i))
    return next


# Main execution
maze = read_maze("input.txt")
R, C = len(maze), len(maze[0])
start = find_start()

pos_set = set()
pos_set.add(start)

# print_maze(pos_set)

for _ in range(64):
    pos_set = do_step(pos_set)
    # print_maze(pos_set)

print(len(pos_set))  # 3762
