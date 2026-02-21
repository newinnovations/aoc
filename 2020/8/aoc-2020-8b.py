#!/usr/bin/env python3

with open(0) as f:
    mem = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]


def boot_is_good(mem):
    used = [False for _ in range(len(mem))]
    acc = pc = 0
    while True:
        if pc == len(mem):
            return acc
        if pc > len(mem) or used[pc]:
            return None
        inst, oper = mem[pc]
        used[pc] = True
        if inst == "jmp":
            pc += oper
        else:
            pc += 1
        if inst == "acc":
            acc += oper


for i in range(len(mem)):
    inst, oper = mem[i]
    if inst == "acc":
        continue

    if inst == "nop":
        mem[i] = ("jmp", oper)
    else:
        mem[i] = ("nop", oper)

    acc = boot_is_good(mem)
    if acc is not None:
        print(acc)  # 552
        break

    mem[i] = (inst, oper)
