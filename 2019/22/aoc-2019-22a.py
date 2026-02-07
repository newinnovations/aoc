#!/usr/bin/env python3

M = 10007

deck = [n for n in range(M)]


def deal_into_new_stack(deck):
    return deck[::-1]


def deal_with_increment(deck, inc):
    ndeck = [-1 for _ in range(M)]
    for i, d in enumerate(deck):
        ndeck[(i * inc) % M] = d
    return ndeck


def cut(deck, c):
    return deck[c:] + deck[:c]


total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        if "new" in line:
            deck = deal_into_new_stack(deck)
        elif "increment" in line:
            deck = deal_with_increment(deck, int(line.split()[-1]))
        elif "cut" in line:
            deck = cut(deck, int(line.split()[-1]))

print(deck.index(2019))  # 1822
