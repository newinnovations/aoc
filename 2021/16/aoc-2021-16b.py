#!/usr/bin/env python3

B = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.


def parse(p):
    version = int(p[:3], 2)
    type = int(p[3:6], 2)
    print(f"version = {version}, type = {type}")
    p = p[6:]

    if type == 4:
        value, has_next = 0, True
        while has_next:
            has_next = p[0] == "1"
            value *= 16
            value += int(p[1:5], 2)
            p = p[5:]
        print("literal", value)
        return p, value
    else:
        values = []
        if p[0] == "0":
            # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            n = int(p[1:16], 2)
            sub = p[16 : 16 + n]
            while sub:
                sub, v = parse(sub)
                values.append(v)
            p = p[16 + n :]
        else:
            # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            n = int(p[1:12], 2)
            p = p[12:]
            for _ in range(n):
                p, v = parse(p)
                values.append(v)
        print(f"operator = {type}, values = {values}")
        if type == 0:
            return p, sum(values)
        elif type == 1:
            value = 1
            for v in values:
                value *= v
            return p, value
        elif type == 2:
            return p, min(values)
        elif type == 3:
            return p, max(values)
        elif type == 5:
            assert len(values) == 2
            return p, int(values[0] > values[1])
        elif type == 6:
            assert len(values) == 2
            return p, int(values[0] < values[1])
        elif type == 7:
            assert len(values) == 2
            return p, int(values[0] == values[1])
        else:
            raise ValueError(type)

    return p


with open(0) as f:
    line = f.read().strip()
    print(line)

# line = "C200B40A82"  # finds the sum of 1 and 2, resulting in the value 3.
# line = "04005AC33890"  # finds the product of 6 and 9, resulting in the value 54.
# line = "880086C3E88112"  # finds the minimum of 7, 8, and 9, resulting in the value 7.
# line = "CE00C43D881120"  # finds the maximum of 7, 8, and 9, resulting in the value 9.
# line = "D8005AC2A8F0"  # produces 1, because 5 is less than 15.
# line = "F600BC2D8F"  # produces 0, because 5 is not greater than 15.
# line = "9C005AC2F8F0"  # produces 0, because 5 is not equal to 15.
# line = "9C0141080250320F1802104A08"  # produces 1, because 1 + 3 = 2 * 2.

p = "".join(B[c] for c in line)
_, value = parse(p)
print(value)  # 246761930504
