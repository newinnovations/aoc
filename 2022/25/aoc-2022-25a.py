#!/usr/bin/env python3


def snafu_dec(snafu):
    d = 0
    for s in snafu:
        d *= 5
        if s == "=":
            d -= 2
        elif s == "-":
            d -= 1
        else:
            d += int(s)
    return d


def dec_snafu(dec):
    if dec == 0:
        return "0"
    digits = ""
    while dec:
        d = int(dec % 5)
        if d > 2:
            d = d - 5
        digits += "012=-"[d]
        dec = (dec - d) // 5
    return digits[::-1]


total = 0
with open(0) as f:
    for line in f:
        total += snafu_dec(line.strip())
print(dec_snafu(total))  # 2-=0-=-2=111=220=100
