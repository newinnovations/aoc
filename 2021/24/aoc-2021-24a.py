#!/usr/bin/env python3

from itertools import product


def variant_1(w, z, _, b):
    return z * 26 + w + b


def variant_2(w, z, a, b):
    x = z % 26 + a
    z //= 26
    if x != w:  # key insight: w must be equal to x to bring z to 0 in the end
        z = z * 26 + w + b
    return z


def run(program, w, z):
    def arg(a):
        if a in "wxyz":
            return regs[ord(a) - ord("w")]
        else:
            return int(a)

    regs = [w, 0, 0, z]
    for i in program:
        p = i.split()
        reg = ord(p[1]) - ord("w")
        if p[0] == "mul":
            res = regs[reg] * arg(p[2])
        elif p[0] == "add":
            res = regs[reg] + arg(p[2])
        elif p[0] == "mod":
            res = regs[reg] % arg(p[2])
        elif p[0] == "div":
            res = regs[reg] // arg(p[2])
        elif p[0] == "eql":
            res = int(regs[reg] == arg(p[2]))
        else:
            raise ValueError("Unkown inst")
        regs[reg] = res
        # print(i, regs)
    return regs[3]


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

# for p in programs:
#     r = ";".join(p)
#     r = r.replace("inp w", "w=n")
#     r = r.replace("mul x 0;add x z;mod x 26;div z 1;add x ", "x=z%26+")
#     r = r.replace("mul x 0;add x z;mod x 26;div z 26;add x ", "x=z%26;z=z//26;x=x")
#     r = r.replace("eql x w;eql x 0", "x=(x!=w)")
#     r = r.replace("mul y 0;add y 25;mul y x;add y 1;mul z y", "z=z*(25*x+1)")
#     # r = r.replace("mul y 0;add y w;add y 12;mul y x;add z y", "z=z+(w+12)*x")
#     r = r.replace("mul y 0;add y w;add y ", "z=z+(w+")
#     r = r.replace(";mul y x;add z y", ")*x")
#     print(r)

# print(programs[0])
# for i in range(26):
#     print(run(programs[0], 5, 28 + i), variant_1(5, 28 + i, *prog2[0]))

# print(programs[3])
# for i in range(26):
#     print(run(programs[3], 5, 27825 + i), variant_2(5, 27825 + i, *prog2[3]))

if False:  # Brute force
    for i in product(range(9, 0, -1), repeat=7):
        z, inp, res = 0, 0, []
        for a, b in prog_params:
            if a < 0:
                w = z % 26 + a
                if w < 1 or w > 9:
                    break
                z //= 26
                res.append(w)
            else:
                w = i[inp]
                res.append(w)
                z = z * 26 + w + b
                inp += 1
        else:
            if z == 0:
                print("".join(map(str, res)))  # 39999698799429
                break

# Other insight: the modulo "thing" connects two digits
stack, related, number = [], [], ["" for _ in range(14)]
for i, (a, b) in enumerate(prog_params):
    if a > 0:
        stack.append((i, b))
    else:
        f, fb = stack.pop()
        related.append((f, i, fb + a))
for f, s, d in sorted(related):  # first, second digit and difference
    n = min(9, 9 - d)
    number[f] = str(n)
    number[s] = str(n + d)
print("".join(number))  # 39999698799429
