#!/usr/bin/env python3

from functools import cache


@cache
def check(msg, rule_no):
    rule = RULES[rule_no]
    if len(rule) == 1:
        if rule[0] == '"a"':
            return msg == "a"
        elif rule[0] == '"b"':
            return msg == "b"
        else:
            return check(msg, rule[0])
    elif len(rule) == 2:
        for s in range(1, len(msg)):
            if check(msg[:s], rule[0]) and check(msg[s:], rule[1]):
                return True
        return False
    elif "|" in rule and len(rule) == 3:
        return check(msg, rule[0]) or check(msg, rule[2])
    elif "|" in rule and len(rule) == 5:
        for s in range(1, len(msg)):
            if check(msg[:s], rule[0]) and check(msg[s:], rule[1]):
                return True
            if check(msg[:s], rule[3]) and check(msg[s:], rule[4]):
                return True
        return False
    else:
        raise ValueError(f"unsupported rule {rule}")


RULES = dict()
with open(0) as f:
    rules, messages = f.read().split("\n\n")

    for r in rules.splitlines():
        r = r.split(": ")
        r1 = r[1].split()
        RULES[r[0]] = r1
    print(RULES)

    messages = messages.splitlines()

# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

RULES["8"] = ["42", "|", "8b"]
RULES["8b"] = ["42", "8"]
RULES["11"] = ["42", "31", "|", "42", "11b"]
RULES["11b"] = ["11", "31"]

print(sum(check(msg, "0") for msg in messages))  # 314
