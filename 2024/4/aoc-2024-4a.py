#!/usr/bin/env python3

total = 0
with open(0) as f:
    puzzle = [line.strip() for line in f]
    size = len(puzzle)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for x in range(size):
                for y in range(size):
                    total += (
                        x + 3 * dx >= 0
                        and y + 3 * dy >= 0
                        and x + 3 * dx < size
                        and y + 3 * dy < size
                        and (puzzle[y][x] == "X")
                        and (puzzle[y + dy][x + dx] == "M")
                        and (puzzle[y + 2 * dy][x + 2 * dx] == "A")
                        and (puzzle[y + 3 * dy][x + 3 * dx] == "S")
                    )
print(total)  # 2336
