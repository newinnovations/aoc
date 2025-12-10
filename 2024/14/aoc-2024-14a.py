#!/usr/bin/env python3

robots = list()
with open("input.txt") as f:
    for line in f:
        px, py, vx, vy = map(
            int, line.strip().replace("p=", "").replace(" v=", ",").split(",")
        )
        robots.append([px, py, vx, vy])

W, H = 101, 103

seconds = 100
end_state = [
    [(px + seconds * vx) % W, (py + seconds * vy) % H] for px, py, vx, vy in robots
]

MID_W = W // 2
MID_H = H // 2

quadrants = [0] * 4
for w, h in end_state:
    if w == MID_W or h == MID_H:
        continue
    quadrant = int(w > MID_W) + 2 * int(h > MID_H)
    quadrants[quadrant] += 1


total = 1
for c in quadrants:
    total *= c
print(total)  # 231852216
