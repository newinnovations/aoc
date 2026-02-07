#!/usr/bin/env python3

from collections import defaultdict

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
J = CARDS.index("J")


def score(hand):
    h = [CARDS.index(c) for c in hand]
    # print(hand, h)
    d = defaultdict(int)
    for c in h:
        d[c] += 1
    j = d[J]
    d[J] = 0
    # print(d)
    two_pair = sum(n == 2 for n in d.values()) == 2
    # Five of a kind, where all five cards have the same label: AAAAA
    if (
        5 in d.values()
        or (4 in d.values() and j == 1)
        or (3 in d.values() and j == 2)
        or (2 in d.values() and j == 3)
        or (1 in d.values() and j == 4)
        or j == 5
    ):
        return tuple([0] + h)
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if (
        4 in d.values()
        or (3 in d.values() and j == 1)
        or (2 in d.values() and j == 2)
        or (1 in d.values() and j == 3)
    ):
        return tuple([1] + h)
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # if 2 in d.values() and 3 in d.values():
    if (
        (2 in d.values() and 3 in d.values())
        or (two_pair and j == 1)
        or (3 in d.values() and j == 2)
        or (2 in d.values() and j == 3)
    ):
        return tuple([2] + h)
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    if 3 in d.values() or (2 in d.values() and j == 1) or (1 in d.values() and j == 2):
        return tuple([3] + h)
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if two_pair or (2 in d.values() and j == 1):
        return tuple([4] + h)
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if 2 in d.values() or j == 1:
        return tuple([5] + h)
    # High card, where all cards' labels are distinct: 23456
    return tuple([6] + h)


hands = {}
with open(0) as f:
    for line in f:
        hand, bid = line.strip().split(" ")
        hands[score(hand)] = (hand, int(bid))

winnings = 0
for rank, strength in enumerate(reversed(sorted(hands.keys()))):
    hand, bid = hands[strength]
    winnings += (rank + 1) * bid
print(winnings)  # 243101568
