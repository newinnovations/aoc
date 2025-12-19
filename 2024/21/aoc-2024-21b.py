#!/usr/bin/env python3
import math
from functools import cache

NUMPAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "X": (3, 0),  # hole
    "0": (3, 1),
    "A": (3, 2),
}

DIRPAD = {
    "X": (0, 0),  # hole
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

DEVICES = {"NUM": NUMPAD, "DIR": DIRPAD}


def straight(b, e):
    (br, bc), (er, ec) = b, e
    if br < er:
        return "v" * (er - br)
    elif br > er:
        return "^" * (br - er)
    elif bc < ec:
        return ">" * (ec - bc)
    elif bc > ec:
        return "<" * (bc - ec)
    else:
        return ""


def move_options(device, b_key, e_key):
    """
    All valid shortest paths (as strings with trailing 'A') from b_key to e_key,
    disallowing stepping onto or crossing the hole 'X'.
    """
    b, e = device[b_key], device[e_key]
    (br, bc), (er, ec) = b, e

    if br == er or bc == ec:
        return [straight(b, e) + "A"]

    options = []
    for corner in [(br, ec), (er, bc)]:
        if device["X"] != corner:
            options.append(straight(b, corner) + straight(corner, e) + "A")
    return options


@cache
def min_cost(device_name, start_key, end_key, layers):
    """
    Minimal presses to go from start_key to end_key on device_name,
    with 'layers' directional-pad layers beneath.
    """
    device = DEVICES[device_name]
    paths = move_options(device, start_key, end_key)
    if not paths:
        return math.inf

    # Base layer: directly count characters
    if layers == 0:
        return min(len(p) for p in paths)

    # Each path p must be "typed" by the next DIR layer as a whole sequence,
    # starting from 'A' and carrying the cursor between characters.
    best = math.inf
    for p in paths:
        cur = "A"
        cost = 0
        for ch in p:
            cost += min_cost("DIR", cur, ch, layers - 1)
            cur = ch
        if cost < best:
            best = cost
    return best


def code_cost(code, layers):
    prev = "A"
    total = 0
    for key in code:
        total += min_cost("NUM", prev, key, layers)
        prev = key
    return total


def complexity(codes, layers):
    total = 0
    for code in codes:
        length = code_cost(code, layers)
        print(code, length)
        total += int(code[:-1]) * length
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        codes = [line.strip() for line in f if line.strip()]
    print(complexity(codes, layers=2))  # 217662
    print(complexity(codes, layers=25))  # 263617786809000
