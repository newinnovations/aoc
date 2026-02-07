#!/usr/bin/env python3

wins = []
with open(0) as f:
    total = 0
    for line in f:
        line = line.strip().split()
        p = line.index("|")
        winning = list(map(int, line[2:p]))
        have = list(map(int, line[p + 1 :]))
        win = 0
        for h in have:
            if h in winning:
                win += 1
        wins.append(win)

cards = {i: 1 for i in range(len(wins))}

for w, win in enumerate(wins):
    for i in range(win):
        if w + i + 1 < len(wins):
            cards[w + i + 1] += cards[w]

print(sum(cards.values()))  # 6420979
