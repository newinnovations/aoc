#!/usr/bin/env python3

total = 0
with open(0) as f:
    puzzle = [line.strip() for line in f]
    size = len(puzzle)
    for x in range(1, size - 1):
        for y in range(1, size - 1):
            total += (
                puzzle[y][x] == "A"
                and (
                    (puzzle[y - 1][x - 1] == "M" and puzzle[y + 1][x + 1] == "S")
                    or (puzzle[y - 1][x - 1] == "S" and puzzle[y + 1][x + 1] == "M")
                )
                and (
                    (puzzle[y + 1][x - 1] == "M" and puzzle[y - 1][x + 1] == "S")
                    or (puzzle[y + 1][x - 1] == "S" and puzzle[y - 1][x + 1] == "M")
                )
            )
print(total)  # 1831
