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

tickets = list()
for ticket in nbt.splitlines()[1:]:
    ticket = list(map(int, ticket.split(",")))
    for t in ticket:
        if not is_ok(t):
            break
    else:
        tickets.append(ticket)

possible = dict()
for pos, numbers in enumerate(zip(*tickets)):
    possible_fields = set(fields.keys())
    for k, (f1, t1, f2, t2) in fields.items():
        for n in numbers:
            if not (f1 <= n <= t1 or f2 <= n <= t2):
                possible_fields.remove(k)
                break
    possible[pos] = possible_fields

cont = True
while cont:
    cont = False
    for k, v in possible.items():
        if len(v) == 1:
            item = list(v)[0]
            for k1, v1 in possible.items():
                if k != k1 and item in v1:
                    v1.remove(item)
                    cont = True

ticket = list(map(int, yt.splitlines()[1].split(",")))
total = 1
for k, v in possible.items():
    print(k, v)
    if "departure" in v.pop():
        total *= ticket[k]

print(total)  # 4381476149273
