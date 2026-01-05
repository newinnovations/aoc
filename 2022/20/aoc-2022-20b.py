#!/usr/bin/env python3


def idx_of_id(n, id):
    for idx, (_, i) in enumerate(n):
        if id == i:
            return idx
    raise ValueError("id not found")


def idx_of_zero(n):
    for idx, (val, _) in enumerate(n):
        if val == 0:
            return idx
    raise ValueError("zero not found")


n = [(int(line.strip()) * 811589153, id) for id, line in enumerate(open(0))]

for _ in range(10):
    for id in range(len(n)):
        idx = idx_of_id(n, id)
        a, _ = n.pop(idx)
        insert = (idx + a) % len(n)
        if insert == 0:
            n.append((a, id))
        else:
            n.insert(insert, (a, id))

idx = idx_of_zero(n)
v1, _ = n[(idx + 1000) % len(n)]
v2, _ = n[(idx + 2000) % len(n)]
v3, _ = n[(idx + 3000) % len(n)]
print(v1 + v2 + v3)  # 4979911042808
