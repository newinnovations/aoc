#!/usr/bin/env python3

vars, opers = dict(), dict()
with open("input.txt") as f:
    for line in f:
        if ":" in line:
            s = line.strip().split(": ")
            vars[s[0]] = s[1] == "1"
        if "-" in line:
            var1, op, var2, _, out = line.strip().split(" ")
            opers[out] = (var1, op, var2)

while True:
    changed = False
    for out, (var1, op, var2) in opers.items():
        if var1 in vars.keys() and var2 in vars.keys() and out not in vars.keys():
            if op == "OR":
                w = vars[var1] or vars[var2]
            elif op == "AND":
                w = vars[var1] and vars[var2]
            else:
                w = vars[var1] != vars[var2]
            vars[out] = w
            changed = True
    if not changed:
        break

bits = []
for i in range(len(vars.keys())):
    name = f"z{i:02}"
    if name not in vars.keys():
        break
    bits.append(vars[name])

value = 0
for bit in bits[::-1]:
    value *= 2
    if bit:
        value += 1

print(value)
