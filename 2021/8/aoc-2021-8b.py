#!/usr/bin/env python3

from collections import defaultdict

S7 = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

S7_INV = {v: k for k, v in S7.items()}


def eliminate(a, b, cannot):
    for x in b:
        cannot[x] |= set(S7[8]) - set(a)


def test(input, output):
    cannot = defaultdict(set)
    for digit in (input + output).split():
        if len(digit) == 2:
            eliminate(digit, S7[1], cannot)
        elif len(digit) == 3:
            eliminate(digit, S7[7], cannot)
        elif len(digit) == 4:
            eliminate(digit, S7[4], cannot)
        elif len(digit) == 5:
            # 2 lacks b,f
            # 3 lacks b,e
            # 5 lacks c,e
            # must contain a,d,g
            eliminate(digit, "adg", cannot)
        elif len(digit) == 6:
            # 6 lacks c
            # 0 lacks d
            # 9 lacks e
            # must contain a,b,f,g
            eliminate(digit, "abfg", cannot)

    mapping = dict()  # wrong --> good
    while len(mapping) < 7:
        for k, v in cannot.items():
            if len(v) == 6:
                mapping[(set(S7[8]) - v).pop()] = k
        for k, v in mapping.items():
            for i in set(S7[8]) - set([v]):
                cannot[i].add(k)

    total = 0
    for digit in output.split():
        remapped = "".join(sorted([mapping[i] for i in digit]))
        total = total * 10 + S7_INV[remapped]
    return total


total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        input, output = line.split("| ")
        total += test(input, output)
print(total)  # 1091609
