#!/usr/bin/env python3

from collections import deque

M = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}

S = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def check_line(line):
    q = deque()
    for ch in line:
        if ch in "([{<":
            q.append(ch)
        elif not q or q.pop() != M[ch]:
            return ch
    return None


total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        incorrent_token = check_line(line)
        if incorrent_token:
            total += S[incorrent_token]

print(total)  # 268845
