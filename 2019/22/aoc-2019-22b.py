#!/usr/bin/env python3


# See README.md
def k_times(k, n0, A, B, M):
    ak = pow(A, k, M)
    bk = (B * (ak - 1) * pow(A - 1, -1, M)) % M
    return (ak * n0 + bk) % M


def combine_instructions_forward():
    a = 1
    b = 0
    for line in lines:
        if "new" in line:
            a *= -1
            b = -b - 1
        elif "increment" in line:
            a *= int(line.split()[-1])
            b *= int(line.split()[-1])
        elif "cut" in line:
            b -= int(line.split()[-1])
        a, b = a % M, b % M
    return a, b


def combine_instructions_reverse():
    a = 1
    b = 0
    for line in lines[::-1]:
        if "new" in line:
            a *= -1
            b = -b - 1
        elif "increment" in line:
            inv_inc = pow(int(line.split()[-1]), -1, M)
            a *= inv_inc
            b *= inv_inc
        elif "cut" in line:
            b += int(line.split()[-1])
        a, b = a % M, b % M
    return a, b


def k_time_forward(k, card_pos):
    return k_times(k, card_pos, *combine_instructions_forward(), M)


def k_time_reverse(k, card_pos):
    return k_times(k, card_pos, *combine_instructions_reverse(), M)


total = 0
with open(0) as f:
    lines = [line.strip() for line in f]


M = 10007
print(k_time_forward(1, 2019))
print(k_time_forward(2, 2019))
print(k_time_forward(1, k_time_forward(1, 2019)))
print(k_time_reverse(1, 1822))
print(k_time_reverse(2, 4556))
print(k_time_reverse(1, k_time_reverse(1, 4556)))

M = 119315717514047
S = 101741582076661
print(k_time_reverse(S, 2020))


# Alternative: instead of deriving the formula, use recursive function taken from
#
# https://github.com/metalim/adventofcode.2019.python/blob/master/22_cards_shuffle.ipynb
#
# modpow the polynomial: (ax+b)^k % M
# f(x) = ax + b
# g(x) = cx + d
# f^2(x) = a(ax + b) + b = aax + ab + b
# f(g(x)) = a(cx + d) + b = acx + ad + b
def polypow(a, b, k, M):
    if k == 0:
        return 1, 0
    if k % 2 == 0:
        return polypow(a * a % M, (a * b + b) % M, k // 2, M)
    else:
        c, d = polypow(a, b, k - 1, M)
        return a * c % M, (a * d + b) % M


a, b = polypow(*combine_instructions_reverse(), S, M)
print((2020 * a + b) % M)
