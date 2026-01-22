#!/usr/bin/env python3

with open(0) as f:
    player_pos = [int(line.strip().split()[-1]) for line in f]

player_score = [0 for _ in player_pos]

cont, rolls = True, 0

while cont:
    for p in range(2):
        throw = 0
        for _ in range(3):
            throw += 1 + rolls % 100
            rolls += 1
        newp = 1 + (player_pos[p] + throw - 1) % 10
        player_pos[p] = newp
        player_score[p] += newp
        if player_score[p] >= 1000:
            print(player_score[1 - p] * rolls)  # 432450
            cont = False
            break
