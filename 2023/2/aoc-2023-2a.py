#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        game_no, game = line.strip().split(": ")
        game_no = int(game_no[5:])
        game_sets = game.split("; ")
        for gs in game_sets:
            d = {
                color: int(cnt) for cnt, color in [c.split(" ") for c in gs.split(", ")]
            }
            if d.get("red", 0) > 12 or d.get("green", 0) > 13 or d.get("blue", 0) > 14:
                break
        else:
            total += game_no
print(total)  # 2285
