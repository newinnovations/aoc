#!/usr/bin/env python3

opers, swap = dict(), dict()


class NeedsSwap(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(f"Need to swap '{self.a}' and {self.b}")


def find(in1, oper, in2):
    global opers, must_swap
    for out, (i1, op, i2) in opers.items():
        if op == oper and ((in1 == i1 and in2 == i2) or (in1 == i2 and in2 == i1)):
            return out
    if cp := swap_counterpart(in1, oper):
        raise NeedsSwap(in2, cp)
    elif cp := swap_counterpart(in2, oper):
        raise NeedsSwap(in1, cp)


def swap_counterpart(input, oper):
    for _, (i1, op, i2) in opers.items():
        if op == oper:
            if i1 == input:
                return i2
            elif i2 == input:
                return i1
    return None  # should not happen


# Try to build the adder device and check if the required operations on the wires are available
#
# If a required operation between two wires is not available it is because one of the wires was swapped. In this case we raise a NeedsSwap exception
#
# We find out which wire is swapped by looking for the requested operation on the other wire
#
# z00 ('y00', 'XOR', 'x00')
# z01 (('x01', 'XOR', 'y01'), 'XOR', ('y00', 'AND', 'x00'))
# z02 (('x02', 'XOR', 'y02'), 'XOR', (('x01', 'AND', 'y01'), 'OR', (('x01', 'XOR', 'y01'), 'AND', ('y00', 'AND', 'x00'))))
# z03 (('x03', 'XOR', 'y03'), 'XOR', (('y02', 'AND', 'x02'), 'OR', (('x02', 'XOR', 'y02'), 'AND', (('x01', 'AND', 'y01'), 'OR', (('x01', 'XOR', 'y01'), 'AND', ('y00', 'AND', 'x00'))))))
# and so on
def check_device_is_adder():
    global opers
    with open("input.txt") as f:
        opers.clear()
        for line in f:
            if "-" in line:
                var1, op, var2, _, out = line.strip().split(" ")
                out = swap.get(out, out)
                opers[out] = (var1, op, var2)

    num_outputs = sum([w[0] == "z" for w in opers.keys()])

    input_xor = dict()
    for i in range(num_outputs - 1):
        input_xor[i] = find(f"x{i:02}", "XOR", f"y{i:02}")

    input_and = dict()
    for i in range(num_outputs - 1):
        input_and[i] = find(f"x{i:02}", "AND", f"y{i:02}")

    carry, som = dict(), dict()
    carry[0] = input_and[0]
    som[0] = input_xor[0]
    som[1] = find(input_xor[1], "XOR", carry[0])
    for i in range(2, num_outputs):
        and_term = find(input_xor[i - 1], "AND", carry[i - 2])
        carry[i - 1] = find(input_and[i - 1], "OR", and_term)
        if i == num_outputs - 1:
            som[i] = carry[i - 1]
        else:
            som[i] = find(input_xor[i], "XOR", carry[i - 1])


while True:
    try:
        check_device_is_adder()
        break
    except NeedsSwap as s:
        print(s)
        swap[s.a] = s.b
        swap[s.b] = s.a

print(",".join(sorted(swap.keys())))  # cqr,ncd,nfj,qnw,vkg,z15,z20,z37
