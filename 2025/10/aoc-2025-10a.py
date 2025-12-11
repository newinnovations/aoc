#!/usr/bin/env python3

from itertools import product


def solve(buttons, target_lights):
    """try to find the number of buttons to press to reach the target"""
    try_max = 2
    num_buttons = len(buttons)
    while True:
        ranges = [list(range(try_max)) for _ in range(num_buttons)]
        minimum = 1e22
        for x in product(*ranges):
            lights = [False] * len(target_lights)
            for button, press in enumerate(x):
                if press % 2:
                    for light in buttons[button]:
                        lights[light] = not (lights[light])
            if lights == target_lights:
                if sum(x) < minimum:
                    minimum = sum(x)
        if minimum < 1e21:
            return minimum
        try_max += 1


total = 0
with open("input.txt") as f:
    for line in f:
        p = line.strip().split(" ")
        # buttons indicate which light each button toggles
        buttons = [list(map(int, b[1:-1].split(","))) for b in p[1:-1]]
        # these are the target values
        target_lights = [x == "#" for x in p[0][1:-1]]
        num_presses = solve(buttons, target_lights)
        total += num_presses
print(total)  # 520
