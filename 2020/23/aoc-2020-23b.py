#!/usr/bin/env python3

N = 1000000

with open(0) as f:
    cups = list(map(int, f.read().strip()))

next_of = [(i + 1) % N for i in range(N)]
for i in range(len(cups)):
    p = cups.index(i + 1)
    ni = cups[(p + 1) % len(cups)]
    next_of[i] = ni - 1

next_of[cups[-1] - 1] = len(cups)
next_of[N - 1] = cups[0] - 1

current = cups[0] - 1

for step in range(10000000):

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

cup1 = next_of[0]
cup2 = next_of[cup1]
print((cup1 + 1) * (cup2 + 1))  # 565615814504
