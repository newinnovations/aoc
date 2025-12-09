#!/usr/bin/env python3

from itertools import pairwise


def get_plant_plot(x, y):
    inside = x >= 0 and y >= 0 and x < size and y < size
    plant = plants[y][x] if inside else ""
    plot = plots[y][x] if inside else -1
    return (plant, plot)


def plot(x, y):
    return plots[y][x] if x >= 0 and y >= 0 and x < size and y < size else -1


def add_to_plot(x, y, p):
    c = plants[y][x]
    plots[y][x] = p
    if get_plant_plot(x + 1, y) == (c, -1):
        add_to_plot(x + 1, y, p)
    if get_plant_plot(x - 1, y) == (c, -1):
        add_to_plot(x - 1, y, p)
    if get_plant_plot(x, y + 1) == (c, -1):
        add_to_plot(x, y + 1, p)
    if get_plant_plot(x, y - 1) == (c, -1):
        add_to_plot(x, y - 1, p)


def num_sides(a):
    if len(a) < 2:
        return len(a)
    return 1 + sum([p2 != p1 + 1 for p1, p2 in pairwise(a)])


def calc_sides(p):
    sides = 0
    for y in range(size):
        top = [x for x in range(size) if plot(x, y) == p and plot(x, y - 1) != p]
        bottom = [x for x in range(size) if plot(x, y) == p and plot(x, y + 1) != p]
        sides += num_sides(top) + num_sides(bottom)
    for x in range(size):
        left = [y for y in range(size) if plot(x, y) == p and plot(x - 1, y) != p]
        right = [y for y in range(size) if plot(x, y) == p and plot(x + 1, y) != p]
        sides += num_sides(left) + num_sides(right)
    return sides


def find_first_free():
    for y in range(size):
        for x in range(size):
            if plots[y][x] == -1:
                return (x, y)
    return None


with open("input.txt") as f:
    plants = [list(line.strip()) for line in f]

size = len(plants)

plots = [[-1] * size for _ in range(size)]
num_plot = 0
while True:
    if (xy := find_first_free()) is None:
        break
    x, y = xy
    add_to_plot(x, y, num_plot)
    num_plot += 1

total = 0
for p in range(num_plot):
    area = sum([plots[y][x] == p for x in range(size) for y in range(size)])
    cost = area * calc_sides(p)
    total += cost

print(total)  # 855082
