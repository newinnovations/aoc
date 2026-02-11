#!/usr/bin/env python3

with open(0) as f:
    lines = f.read().splitlines()

depart = int(lines[0])
ids = lines[1].split(",")
ids = [int(id) for id in ids if id != "x"]

d = depart
while True:
    for id in ids:
        if d % id == 0:
            print((d - depart) * id)  # 2305
            break
    else:
        d += 1
        continue
    break
