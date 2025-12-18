#!/usr/bin/env python3

reg_a, reg_b, reg_c, program = 0, 0, 0, []
with open("input.txt") as f:
    for line in f:
        if line.startswith("Register A:"):
            reg_a = int(line[12:])
        if line.startswith("Register B:"):
            reg_b = int(line[12:])
        if line.startswith("Register C:"):
            reg_c = int(line[12:])
        if line.startswith("Program:"):
            program = list(map(int, line[9:].split(",")))


def combo_operand(oper, reg):
    if oper > 3:
        return reg[oper - 4]
    return oper


def execute(program, reg_a, reg_b, reg_c):
    # print(reg_a, reg_b, reg_c, program)
    reg, pc, output = [reg_a, reg_b, reg_c], 0, []
    while pc < len(program):
        inst, oper, pc = program[pc], program[pc + 1], pc + 2
        if inst == 0:
            reg[0] = reg[0] // (2 ** combo_operand(oper, reg))
        elif inst == 1:
            reg[1] = reg[1] ^ oper
        elif inst == 2:
            reg[1] = combo_operand(oper, reg) % 8
        elif inst == 3:
            if reg[0]:
                pc = oper
        elif inst == 4:
            reg[1] = reg[1] ^ reg[2]
        elif inst == 5:
            output.append(combo_operand(oper, reg) % 8)
        elif inst == 6:
            reg[1] = reg[0] // (2 ** combo_operand(oper, reg))
        elif inst == 7:
            reg[2] = reg[0] // (2 ** combo_operand(oper, reg))
    return output


output = execute(program, reg_a, reg_b, reg_c)
print(",".join(map(str, output)))
