#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        game_no, game = line.strip().split(": ")
        game_no = int(game_no[5:])
        game_sets = game.split("; ")
        needed = [0, 0, 0]
        for gs in game_sets:
            d = {
                color: int(cnt) for cnt, color in [c.split(" ") for c in gs.split(", ")]
            }
            dl = [d.get("red", 0), d.get("green", 0), d.get("blue", 0)]
            needed = [max(a, b) for a, b in zip(needed, dl)]
        power = needed[0] * needed[1] * needed[2]
        total += power
print(total)  # 77021
