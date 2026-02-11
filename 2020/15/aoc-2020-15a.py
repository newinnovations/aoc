#!/usr/bin/env python3

with open(0) as f:
    n = list(map(int, f.read().split(",")))

turn = {i: t for t, i in enumerate(n)}

last = n[-1]
for t in range(len(n), 2020):
    last_turn = turn[last]
    if isinstance(last_turn, int):
        last = 0
    else:
        last = last_turn[1] - last_turn[0]
    if last in turn:
        last_turn = turn[last]
        if isinstance(last_turn, int):
            turn[last] = (last_turn, t)
        else:
            turn[last] = (last_turn[1], t)
    else:
        turn[last] = t
print(last)  # 253
