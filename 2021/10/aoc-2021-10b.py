#!/usr/bin/env python3

from collections import deque

M = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}

S = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def check_line(line):
    q = deque()
    for ch in line:
        if ch in "([{<":
            q.append(ch)
        elif not q or q.pop() != M[ch]:
            return None
    if q:
        res = 0
        for ch in reversed(q):
            res = res * 5 + S[ch]
        return res
    else:
        return None


totals = []
with open(0) as f:
    for line in f:
        line = line.strip()
        score = check_line(line)
        if score is not None:
            totals.append(score)
totals.sort()
print(totals[len(totals) // 2])  # 4038824534
