#!/usr/bin/env python3


def is_ok(n):
    for f1, t1, f2, t2 in fields.values():
        if f1 <= n <= t1 or f2 <= n <= t2:
            return True
    return False


with open(0) as f:
    flds, yt, nbt = f.read().split("\n\n")

fields = dict()
for f in flds.splitlines():
    name, rule = f.split(": ")
    rule = rule.replace(" or", "").replace("-", " ")
    rule = tuple(map(int, rule.split()))
    fields[name] = rule

total = 0
for ticket in nbt.splitlines()[1:]:
    ticket = list(map(int, ticket.split(",")))
    for t in ticket:
        if not is_ok(t):
            total += t

print(total)  # 30869
