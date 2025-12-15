#!/usr/bin/env python3

from functools import cache

with open("input.txt") as f:
    matrix = [list(line.strip()) for line in f]


# def ways(matrix, pos):
#     """Original recursive idea, only works for the small sample data set"""
#     if len(matrix) == 0:
#         return 1
#     else:
#         if matrix[0][pos] == "^":
#             return ways(matrix[1:], pos - 1) + ways(matrix[1:], pos + 1)
#         else:
#             return ways(matrix[1:], pos)


@cache
def ways_recur(row, pos):
    """Improved recursive approach with memoization"""
    if row == len(matrix):
        return 1
    else:
        if matrix[row][pos] == "^":
            return ways_recur(row + 1, pos - 1) + ways_recur(row + 1, pos + 1)
        else:
            return ways_recur(row + 1, pos)


def ways_iter(pos):
    """Non-recursive bottom-up equivalent of the recursive approach"""

    # Base vector: "one row beyond the last" -> 1 way regardless of column
    num_ways = [1] * len(matrix[0])

    for row in matrix[::-1]:  # Iterate from bottom row to top row
        num_ways = [
            num_ways[col - 1] + num_ways[col + 1] if char == "^" else num_ways[col]
            for col, char in enumerate(row)
        ]

    # At the end, num_ways holds the number of ways from the top row for each column
    return num_ways[pos]


start = matrix[0].index("S")
print(ways_recur(0, start))  # 73007003089792
print(ways_iter(start))  # 73007003089792
