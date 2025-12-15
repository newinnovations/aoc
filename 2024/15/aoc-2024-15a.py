#!/usr/bin/env python3


def get_start():
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "@":
                return (x, y)
    raise ValueError("failed to find start")


def can_move(x, y):
    if maze[y][x] == "#":
        return False
    elif maze[y][x] == ".":
        return True
    return can_move(x + dx, y + dy)


# at exit maze(x,y) == "."
def do_move(x, y):
    if maze[y][x] == ".":
        return
    do_move(x + dx, y + dy)
    maze[y + dy][x + dx] = maze[y][x]
    maze[y][x] = "."


maze, dirs = list(), list()
with open("input.txt") as f:
    is_maze = True
    for line in f:
        line = line.strip()
        if not line:
            is_maze = False
        if is_maze:
            maze.append(list(line.strip()))
        else:
            dirs += list(line.strip())

x, y = get_start()

for d in dirs:
    if d == "^":
        dx, dy = 0, -1
    elif d == ">":
        dx, dy = 1, 0
    elif d == "v":
        dx, dy = 0, 1
    else:
        dx, dy = -1, 0

    if can_move(x, y):
        do_move(x, y)
        x, y = x + dx, y + dy

    # print(d, x, y)
    # for m in maze:
    #     print(" ".join(m))
    # print()

print(
    sum(
        y * 100 + x
        for x in range(len(maze[0]))
        for y in range(len(maze))
        if maze[y][x] == "O"
    )
)  # 1526018
