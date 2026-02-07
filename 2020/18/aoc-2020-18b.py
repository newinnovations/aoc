#!/usr/bin/env python3

from ast import literal_eval


def calc(f):
    if isinstance(f, int):
        return f
    else:
        if len(f) == 1:
            return calc(f[0])
        elif f[1] == "+":
            return calc([calc(f[0]) + calc(f[2])] + f[3:])
        elif f[1] == "*":
            return calc([calc(f[0]) * calc(f[2:])])
        else:
            raise ValueError(f[1])


total = 0
with open(0) as f:
    for line in f:
        line = (
            line.strip()
            .replace("+", '"+"')
            .replace("*", '"*"')
            .replace("(", "[")
            .replace(")", "]")
            .replace(" ", ",")
        )

        f = literal_eval(f"[{line}]")

        print(f, calc(f))
        total += calc(f)

print(total)  # 461295257566346
