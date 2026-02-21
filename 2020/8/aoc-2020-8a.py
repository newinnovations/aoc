#!/usr/bin/env python3

with open(0) as f:
    mem = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]

acc = pc = 0
used = [False for _ in range(len(mem))]
while True:
    if used[pc]:
        print(acc)  # 1727
        break
    inst, oper = mem[pc]
    used[pc] = True
    if inst == "jmp":
        pc += oper
    else:
        pc += 1
    if inst == "acc":
        acc += oper
