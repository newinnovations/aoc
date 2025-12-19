#!/usr/bin/env python3

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


def key_presses(device, keys_options):
    all_options = []
    for keys in keys_options:  # goal can be found with any in key_options
        prev = "A"
        options = [""]
        for key in keys:
            m = move_options(device, prev, key)
            options = [o1 + m1 for o1 in options for m1 in m]
            prev = key
        all_options += options
    m = min(len(o) for o in all_options)
    return [o for o in all_options if len(o) == m]


def code_cost(codes, layers):
    k = key_presses(NUMPAD, [codes])
    for _ in range(layers):
        k = key_presses(DIRPAD, k)
    return k


def complexity(codes, layers):
    total = 0
    for code in codes:
        a = code_cost(code, layers)[0]
        print(code, len(a), a)
        total += int(code[:-1]) * len(a)
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        codes = [line.strip() for line in f if line.strip()]
    print(complexity(codes, layers=2))  # 217662
