#!/usr/bin/env python3

import re


def new_range(start, finish):
    return (start, finish) if start < finish else None


def apply_rules(name, range):
    if name in ["A", "R"]:
        mult = 1
        for s, f in range.values():
            mult *= f - s
        return (mult, 0) if name == "A" else (0, mult)
    total = (0, 0)  # accepted, rejected
    for rule in rules[name].split(","):
        if ":" in rule:
            cond, target = rule.split(":")
            (cat, oper), val = cond[:2], int(cond[2:])
            s, f = range[cat]

            hit, not_hit = None, None
            if oper == "<":
                hit = new_range(s, val)
                not_hit = new_range(val, f)
            else:  # >
                not_hit = new_range(s, val + 1)
                hit = new_range(val + 1, f)
            if hit:
                target_range = range.copy()
                target_range[cat] = hit
                total = map(sum, zip(total, apply_rules(target, target_range)))
            range[cat] = not_hit
        else:
            total = map(sum, zip(total, apply_rules(rule, range)))
    return tuple(total)


rules, pattern = {}, re.compile(r"(\w*){(.*)}")
with open("input.txt") as f:
    for line in f:
        if match := pattern.match(line):
            name, data = match.groups()
            if name:
                rules[name] = data

range = {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}
print(apply_rules("in", range)[0])  # 126107942006821
