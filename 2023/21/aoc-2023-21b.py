#!/usr/bin/env python3

from functools import cache
from itertools import pairwise

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_maze(filename):
    maze = []
    with open(filename) as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


@cache
def neighbors(pos):
    r, c = pos
    lst = []
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if maze[nr % R][nc % C] != "#":
            lst.append((nr, nc))
    return lst


def find_start():
    for r_num, r in enumerate(maze):
        if "S" in r:
            c_num = r.index("S")
            return (r_num, c_num)
    return (0, 0)


def print_maze(plot_set):
    for r_num, r in enumerate(maze):
        for c_num, c in enumerate(r):
            if (r_num, c_num) in plot_set:
                print("O", end=" ")
            else:
                print(c, end=" ")
        print()
    print()


def do_step(plot_set):
    next = set()
    for p in plot_set:
        next.update(neighbors(p))
    return next


def num_plots(plot_set, steps):
    for _ in range(steps):
        plot_set = do_step(plot_set)
    num = len(plot_set)
    # print(steps, num)
    return num, plot_set


# https://www.reddit.com/r/adventofcode/comments/18orn0s/2023_day_21_part_2_links_between_days/
def calc_next(s):
    last = []
    d = s
    while True:
        last.append(d[-1])
        d = [b - a for a, b in pairwise(d)]
        if all(n == 0 for n in d):
            break
    return sum(last), last


# Main execution
maze = read_maze("input.txt")
R, C = len(maze), len(maze[0])
start = find_start()

seq = []
plot_set = set()
plot_set.add(start)
num, plot_set = num_plots(plot_set, 65)
seq.append(num)
for n in range(2):
    num, plot_set = num_plots(plot_set, 131)
    seq.append(num)

# print(seq)  # seq = [3868, 34368, 95262]  186550, 308232, 460308

_, (a, b, c) = calc_next(seq)

n = 202300 - 2
print(a + n * b + c * n * (n + 1) // 2)  # 621944727930768

# for i in range(n):
#     b += c
#     a += b
# print(a)  # 621944727930768
