#!/usr/bin/env python3

from collections import deque

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


# 2,4  b = a % 8
# 1,1  b = b xor 1
# 7,5  c = a // 2**b
# 4,4  b = b xor c
# 1,4  b = b xor 4
# 0,3  a = a // 8
# 5,5  out(b % 8)
# 3,0  jnz 0

# reg_a is 48 bits:
# 47..0 determines out
# 44..0 determines out[1:]
#  8..0 determines out[13:]
#  5..0 determines out[14:]
#  2..0 determines out[15]

q = deque([(0, 0)])
while q:
    p, a = q.popleft()
    if p == len(program):
        print(a)
        break
    else:
        a *= 8
        target = program[-1 - p :]
        for i in range(8):
            if target == execute(program, a + i, 0, 0):
                q.append((p + 1, a + i))
