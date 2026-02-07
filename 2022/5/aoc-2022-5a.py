#!/usr/bin/env python3

blocks = open(0).read().split("\n\n")

stacks = [[] for _ in range(10)]
for line in zip(*blocks[0].splitlines()):
    if line[-1] == " ":
        continue
    line = line[::-1]
    stacks[int(line[0])] = [x for x in line[1:] if x != " "]

for line in blocks[1].splitlines():
    s = line.split()
    f, t = int(s[3]), int(s[5])
    for _ in range(int(s[1])):
        item = stacks[f].pop()
        stacks[t].append(item)

print("".join([s[-1] for s in stacks if s]))  # QMBMJDFTD
