#!/usr/bin/env python3

# My method: find the match for two bus lines and the new period
# then apply this to the third to find a new match/period that fits all three
# and so on.


# Assume A has offset 0 --> Match is at a multiple of A, say t = n·A
# At t the offset of B is t mod B. To find the time we are interested in the
# following equation must be valid:
#    t mod B = off_b
#    n·A mod B == off_b
#    n = off_b / A     (mod B)
# In practice A will have an offset not equal to 0. Swift by -off_a to do the
# modulo calcualtion and then shift back.
# This combination will have a period of A·B
def calc(a, b):
    A, off_a = a
    B, off_b = b
    n = ((off_b - off_a) * pow(A, -1, B)) % B
    AB = A * B
    t = off_a + n * A
    return (AB, t)


with open(0) as f:
    lines = f.read().splitlines()

ids = lines[1].split(",")
ids = [(int(id), -pos) for pos, id in enumerate(ids) if id != "x"]

a = ids[0]
for b in ids[1:]:
    a = calc(a, b)
print(a[1])  # 552612234243498


# Chinese Remainder Theorem
# https://www.youtube.com/watch?v=-QhGWpIieCI
M = 1
for id in ids:
    M *= id[0]
a = [id[1] for id in ids]
c = [M // id[0] for id in ids]
b = [pow(ci, -1, idi[0]) for ci, idi in zip(c, ids)]
# print(a, b, c, M)

print(sum(ai * bi * ci for ai, bi, ci in zip(a, b, c)) % M)  # 552612234243498
