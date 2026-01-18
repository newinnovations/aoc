#!/usr/bin/env python3

programs, p = [], []

with open(0) as f:
    for line in f:
        line = line.strip()
        if line == "inp w":
            if p:
                programs.append(p)
                p = []
        else:
            p.append(line)
programs.append(p)

prog_params = []
for p in programs:
    prog_params.append((int(p[4].split()[-1]), int(p[14].split()[-1])))

stack, related, number = [], [], ["" for _ in range(14)]
for i, (a, b) in enumerate(prog_params):
    if a > 0:
        stack.append((i, b))
    else:
        f, fb = stack.pop()
        related.append((f, i, fb + a))
for f, s, d in sorted(related):
    n = max(1, 1 - d)
    number[f] = str(n)
    number[s] = str(n + d)
print("".join(number))  # 18116121134117
