#!/usr/bin/env python3

import re


def do_part(part):
    rule = "in"
    while True:
        # print(part, rule)
        if rule in ["R", "A"]:
            return rule
        for r in rules[rule].split(","):
            if ":" in r:
                cond, target = r.split(":")
                if cond[1] == "<":
                    match = part[cond[0]] < int(cond[2:])
                else:
                    match = part[cond[0]] > int(cond[2:])
                if match:
                    rule = target
                    break
            else:
                rule = r


rules, parts, pattern = {}, [], re.compile(r"(\w*){(.*)}")
with open("input.txt") as f:
    for line in f:
        if match := pattern.match(line):
            name, data = match.groups()
            if name:
                rules[name] = data
            else:
                parts.append(
                    {k: int(v) for (k, v) in [d.split("=") for d in data.split(",")]}
                )

ratings = 0
for part in parts:
    if do_part(part) == "A":
        ratings += sum(part.values())
print(ratings)
