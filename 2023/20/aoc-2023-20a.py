#!/usr/bin/env python3

from collections import defaultdict, deque

inputs = defaultdict(list)
outputs = defaultdict(list)
types = {}


def single_press():
    count = (0, 0)
    d = deque([("button", False, "broadcaster")])
    while d:
        (orig, p, name) = d.popleft()
        count = (count[0] + (not p), count[1] + p)
        if t := types.get(name):
            if t == "%" and p == 0:
                s = not state[name]
                state[name] = s
                for o in outputs[name]:
                    d.append((name, s, o))
            elif t == "&":
                conj_state[name][orig] = p
                s = not all(conj_state[name].values())
                state[name] = s
                for o in outputs[name]:
                    d.append((name, s, o))
        else:
            state[name] = p
            for o in outputs[name]:
                d.append((name, p, o))
    return count


with open("input.txt") as f:
    for line in f:
        name, output = line.strip().split(" -> ")
        output = output.split(", ")
        if name != "broadcaster":
            name = name[1:]
            types[name] = line[0]
        for o in output:
            inputs[o].append(name)
        outputs[name] = output

state = {name: False for name in inputs}
conj_state = {}
for name, type in types.items():
    if type == "&":  # conjunction
        cs = {i: False for i in inputs[name]}
        conj_state[name] = cs


def n_press(n):
    count = (0, 0)
    for _ in range(n):
        c = single_press()
        count = (count[0] + c[0], count[1] + c[1])
    return count


count = n_press(1000)
print(count[0] * count[1])  # 919383692
