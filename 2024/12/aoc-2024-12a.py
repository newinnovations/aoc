#!/usr/bin/env python3


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


def calc_perimeter(p):
    perimeter = 0
    for y in range(size):
        top = [x for x in range(size) if plot(x, y) == p and plot(x, y - 1) != p]
        bottom = [x for x in range(size) if plot(x, y) == p and plot(x, y + 1) != p]
        perimeter += len(top) + len(bottom)
    for x in range(size):
        left = [y for y in range(size) if plot(x, y) == p and plot(x - 1, y) != p]
        right = [y for y in range(size) if plot(x, y) == p and plot(x + 1, y) != p]
        perimeter += len(left) + len(right)
    return perimeter


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
    cost = area * calc_perimeter(p)
    total += cost

print(total)  # 1433460
