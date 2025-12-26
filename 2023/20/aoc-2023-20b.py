#!/usr/bin/env python3

from collections import defaultdict, deque
from math import lcm

inputs = defaultdict(list)
outputs = defaultdict(list)
types = {}


def single_press():
    count = (0, 0)
    d = deque([("button", False, "broadcaster")])
    while d:
        # need to check inside the loop, at the of end of the
        # sequence the signal is back to low
        for i in rx_in:
            if freq[i] is None and state[i]:
                freq[i] = n  # type: ignore
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


rx_in = inputs[inputs["rx"][0]]

# mp 3917, 7834, 11751, 15668, 19585, 23502, 27419
# ng 3919, 7838, 11757, 15676, 19595, 23514, 27433
# qb 4027, 8054, 12081, 16108, 20135, 24162, 28189
# qt 4007, 8014, 12021, 16028, 20035, 24042, 28049

freq = {n: None for n in rx_in}
n = 1
while True:
    single_press()
    if all(f is not None for f in freq.values()):
        break
    n += 1

result = 1
for f in freq.values():
    result = lcm(result, f)  # type: ignore

print(result)
