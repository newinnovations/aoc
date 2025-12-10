#!/usr/bin/env python3

from itertools import product


def solve(buttons, target_counters):
    """try to find the number of buttons to press to reach the target (brute force)"""
    try_max = 2
    num_buttons = len(buttons)
    while True:
        ranges = [list(range(try_max)) for _ in range(num_buttons)]
        minimum = 1e22
        for x in product(*ranges):
            counter_values = [0] * len(target_counters)
            for button, press in enumerate(x):
                for t in buttons[button]:
                    counter_values[t] += press
            if counter_values == target_counters:
                if sum(x) < minimum:
                    minimum = sum(x)
        if minimum < 1e21:
            return minimum
        try_max += 1


total = 0
with open("ref.txt") as f:  # works only on the sample data (ref.txt)
    for line in f:
        parts = line.strip().split(" ")
        # buttons indicate which counters each button increments
        buttons = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
        # these are the target values
        target_counters = list(map(int, parts[-1][1:-1].split(",")))
        num_presses = solve(buttons, target_counters)
        print(num_presses)
        total += num_presses
print(total)  # ??
