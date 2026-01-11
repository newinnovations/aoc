#!/usr/bin/env python3

total = 0
program = []
with open(0) as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            program.append(0)
        else:
            program.append(int(line[5:]))


def show_cycle(cycle, x):
    global total
    if (cycle - 20) % 40 == 0:
        total += cycle * x


pc, x, cycle = 0, 1, 1
while cycle < 221:
    i = program[pc]
    if i:
        show_cycle(cycle, x)
        show_cycle(cycle + 1, x)
        x += i
        cycle += 2
    else:
        show_cycle(cycle, x)
        cycle += 1
    pc += 1


print(total)  # 10760
