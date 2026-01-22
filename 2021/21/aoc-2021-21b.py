#!/usr/bin/env python3

from functools import cache

with open(0) as f:
    player_pos = [int(line.strip().split()[-1]) for line in f]


dice_outcomes = [
    t1 + t2 + t3 for t1 in range(1, 4) for t2 in range(1, 4) for t3 in range(1, 4)
]


@cache
def num_wins(p1_plays, pos1, pos2, score1, score2):
    win_1, win_2 = (0, 0)
    if p1_plays:
        for d in dice_outcomes:
            npos = 1 + (pos1 + d - 1) % 10
            nscore = score1 + npos
            if nscore >= 21:
                win_1 += 1
            else:
                w1, w2 = num_wins(False, npos, pos2, nscore, score2)
                win_1, win_2 = win_1 + w1, win_2 + w2
    else:
        for d in dice_outcomes:
            npos = 1 + (pos2 + d - 1) % 10
            nscore = score2 + npos
            if nscore >= 21:
                win_2 += 1
            else:
                w1, w2 = num_wins(True, pos1, npos, score1, nscore)
                win_1, win_2 = win_1 + w1, win_2 + w2
    return win_1, win_2


wins = num_wins(True, *player_pos, 0, 0)
# print(wins)
print(max(wins))  # 138508043837521
