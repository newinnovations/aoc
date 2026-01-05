#!/usr/bin/env python3

vars, opers = {}, {}
with open(0) as f:
    for line in f:
        s = line.strip().split()
        if len(s) == 2:
            vars[s[0][:-1]] = int(s[1])
        elif len(s) == 4:
            opers[s[0][:-1]] = tuple(s[1:])
        else:
            raise ValueError("incorrect input")

while "root" not in vars.keys():
    to_delete = []
    for c, (a, op, b) in opers.items():
        if a in vars and b in vars:
            vars[c] = eval(f"{vars[a]} {op} {vars[b]}".replace("/", "//"))
            to_delete.append(c)
    for c in to_delete:
        opers.pop(c)

print(vars["root"])  # 353837700405464
