#!/usr/bin/env python3

# Hint: arr[cup] = next_cup

with open(0) as f:
    cups = list(map(int, f.read().strip()))

N = len(cups)

next_of = [cups[(cups.index(i + 1) + 1) % N] - 1 for i in range(N)]

current = cups[0] - 1

for step in range(100):

    first = next_of[current]
    second = next_of[first]
    third = next_of[second]

    destination = (current - 1) % N
    while destination in [first, second, third]:
        destination = (destination - 1) % N

    next_of[current] = next_of[third]
    next_of[third] = next_of[destination]
    next_of[destination] = first

    current = next_of[current]

i = 0
for _ in range(1, N):
    i = next_of[i]
    print(i + 1, end="")
print()  # 78569234
