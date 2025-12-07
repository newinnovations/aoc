#!/usr/bin/env python3

opers, swap, must_swap = dict(), dict(), list()


def find(var1, oper, var2):
    global opers, must_swap
    for wire, (v1, op, v2) in opers.items():
        if op == oper and ((var1 == v1 and var2 == v2) or (var1 == v2 and var2 == v1)):
            return wire
    if var2 and alternative(var1, oper):
        must_swap = [var2, alternative(var1, oper)]
    elif var1 and alternative(var2, oper):
        must_swap = [var1, alternative(var2, oper)]
    return None


def alternative(var, oper):
    for _, (v1, op, v2) in opers.items():
        if op == oper:
            if v1 == var:
                return v2
            elif v2 == var:
                return v1
    return None


# z00 ('y00', 'XOR', 'x00')
# z01 (('x01', 'XOR', 'y01'), 'XOR', ('y00', 'AND', 'x00'))
# z02 (('x02', 'XOR', 'y02'), 'XOR', (('x01', 'AND', 'y01'), 'OR', (('x01', 'XOR', 'y01'), 'AND', ('y00', 'AND', 'x00'))))
# z03 (('x03', 'XOR', 'y03'), 'XOR', (('y02', 'AND', 'x02'), 'OR', (('x02', 'XOR', 'y02'), 'AND', (('x01', 'AND', 'y01'), 'OR', (('x01', 'XOR', 'y01'), 'AND', ('y00', 'AND', 'x00'))))))


def is_device_working():
    global opers, must_swap
    opers.clear()
    must_swap = []
    with open("input.txt") as f:
        for line in f:
            if "-" in line:
                var1, op, var2, _, out = line.strip().split(" ")
                out = swap.get(out, out)
                opers[out] = (var1, op, var2)

    num_wires = sum([w[0] == "z" for w in opers.keys()])

    input_xor = dict()
    for i in range(num_wires):
        input_xor[i] = find(f"x{i:02}", "XOR", f"y{i:02}")
        if must_swap:
            return False

    input_and = dict()
    for i in range(num_wires):
        input_and[i] = find(f"x{i:02}", "AND", f"y{i:02}")
        if must_swap:
            return False

    carry, som = dict(), dict()
    carry[1] = find("x00", "AND", "y00")
    for i in range(2, num_wires):
        and_term = find(input_xor[i - 1], "AND", carry[i - 1])
        if must_swap:
            return False
        carry[i] = find(input_and[i - 1], "OR", and_term)
        if must_swap:
            return False
        som[i] = find(input_xor[i], "XOR", carry[i])
        if must_swap:
            return False

    return True


while True:
    if is_device_working():
        break
    a, b = must_swap
    swap[a] = b
    swap[b] = a

print(",".join(sorted(swap.keys())))
