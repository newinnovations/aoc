#!/usr/bin/env python3

with open(0) as f:
    a, b = f.read().split("\n\n")
    a = tuple(map(int, a.splitlines()[1:]))
    b = tuple(map(int, b.splitlines()[1:]))


def game(a, b):
    seen = set()
    while True:
        if not a or not b:
            break

        if (a, b) in seen:
            # print("infinite escape")
            return "a", a

        seen.add((a, b))

        if len(a) > a[0] and len(b) > b[0]:
            # print("sub", a, b)
            winner, _ = game(a[1 : 1 + a[0]], b[1 : 1 + b[0]])
            # print(winner)
        else:
            winner = "a" if a[0] > b[0] else "b"

        if winner == "a":
            a = a[1:] + (a[0], b[0])
            b = b[1:]
        else:
            b = b[1:] + (b[0], a[0])
            a = a[1:]
    return ("a", a) if a else ("b", b)


_, win_cards = game(a, b)
print(sum((i + 1) * w for i, w in enumerate(win_cards[::-1])))  # 34901
