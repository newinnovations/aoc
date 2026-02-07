#!/usr/bin/env python3


def check_card(card):
    scores = []
    for row in card:
        scores.append([numbers.index(n) for n in row])
    win_at = 100000
    for row in scores:
        win_at = min(win_at, max(row))
    for row in zip(*scores):
        win_at = min(win_at, max(row))
    return win_at


total = 0
with open(0) as f:
    parts = f.read().split("\n\n")
    numbers = list(map(int, parts[0].split(",")))
    cards = [
        [list(map(int, row.split())) for row in card.splitlines()] for card in parts[1:]
    ]

winning, best = cards[0], 0
for i, card in enumerate(cards):
    win_at = check_card(card)
    if best < win_at:
        best = win_at
        winning = card

for row in winning:
    for n in row:
        if numbers.index(n) > best:
            total += n

print(total * numbers[best])  # 22704
