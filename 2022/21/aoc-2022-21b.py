#!/usr/bin/env python3


def forward_solve():
    global vars, opers
    while True:
        to_delete = []
        for c, (a, op, b) in opers.items():
            if a in vars and b in vars:
                vars[c] = eval(f"{vars[a]} {op} {vars[b]}".replace("/", "//"))
                to_delete.append(c)
        if not to_delete:
            break
        for c in to_delete:
            opers.pop(c)


def backward_solve():
    global vars, opers
    while True:
        to_delete = []
        for c, (a, op, b) in opers.items():
            if c in vars:
                if a in vars:
                    if op == "+":  # c=a+b b=c-a
                        res = vars[c] - vars[a]
                    elif op == "-":  # c=a-b b=a-c
                        res = vars[a] - vars[c]
                    elif op == "*":  # c=a*b b=c/a
                        res = vars[c] // vars[a]
                    elif op == "/":  # c=a/b b=a/c
                        res = vars[a] // vars[c]
                    else:
                        raise ValueError("incorrect operation")
                    vars[b] = res
                    to_delete.append(c)
                elif b in vars:
                    if op == "+":  # c=a+b a=c-b
                        res = vars[c] - vars[b]
                    elif op == "-":  # c=a-b a=c+b
                        res = vars[c] + vars[b]
                    elif op == "*":  # c=a*b a=c/b
                        res = vars[c] // vars[b]
                    elif op == "/":  # c=a/b a=c*b
                        res = vars[c] * vars[b]
                    else:
                        raise ValueError("incorrect operation")
                    vars[a] = res
                    to_delete.append(c)
        if not to_delete:
            break
        for c in to_delete:
            opers.pop(c)


vars, opers = {}, {}
term1, term2 = "", ""
with open(0) as f:
    for line in f:
        s = line.strip().split()
        if s[0] == "humn:":
            continue
        if len(s) == 2:
            vars[s[0][:-1]] = int(s[1])
        elif len(s) == 4:
            if s[0] == "root:":
                term1, term2 = s[1], s[3]
            else:
                opers[s[0][:-1]] = tuple(s[1:])
        else:
            raise ValueError("incorrect input")

forward_solve()

if v := vars.get(term1):
    vars[term2] = v
elif v := vars.get(term2):
    vars[term1] = v
else:
    raise ValueError("both terms are unknow")

backward_solve()

print(vars["humn"])  # 3678125408017
