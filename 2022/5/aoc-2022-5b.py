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
    n, f, t = int(s[1]), int(s[3]), int(s[5])
    items = stacks[f][-n:]
    stacks[f] = stacks[f][:-n]
    stacks[t] += items

print("".join([s[-1] for s in stacks if s]))  # NBTVTJNFJ
