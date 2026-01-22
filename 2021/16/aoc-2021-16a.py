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


def parse(p):
    global total
    version = int(p[:3], 2)
    type = int(p[3:6], 2)
    print(f"version = {version}, type={type}")
    total += version
    p = p[6:]

    if type == 4:
        value, has_next = 0, True
        while has_next:
            has_next = p[0] == "1"
            value *= 16
            value += int(p[1:5], 2)
            p = p[5:]
        print("literal", value)
    else:
        if p[0] == "0":
            # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            n = int(p[1:16], 2)
            sub = p[16 : 16 + n]
            while sub:
                sub = parse(sub)
            p = p[16 + n :]
        else:
            # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            n = int(p[1:12], 2)
            p = p[12:]
            for _ in range(n):
                p = parse(p)

    return p


total = 0
with open(0) as f:
    line = f.read().strip()
    print(line)

# line = "D2FE28"
# line = "38006F45291200"
# line = "EE00D40C823060"

# line = "8A004A801A8002F478"  # represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of 16.
# line = "620080001611562C8802118E34"  # represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.
# line = "C0015000016115A2E0802F182340"  # has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of 23.
# line = "A0016C880162017C3686B18A3D4780"  # is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of 31.


p = "".join(B[c] for c in line)
print(parse(p))

print(total)  # 1038
