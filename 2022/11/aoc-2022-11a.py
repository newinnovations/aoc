#!/usr/bin/env python3

monkeys, inspections = [], []
with open(0) as f:
    for block in f.read().split("\n\n"):
        line = block.replace(", ", ",").split()
        # for inspected_max, e in enumerate(line):
        #     print(inspected_max, e)
        monkeys.append(
            [
                list(map(int, line[4].split(","))),
                line[9],  # operator
                line[10],  # number or "old"
                int(line[14]),  # divider
                int(line[20]),  # true
                int(line[26]),  # false
            ]
        )
        inspections.append(0)

for _ in range(20):
    for i, m in enumerate(monkeys):
        for worry in m[0]:
            inspections[i] += 1
            if m[1] == "+":
                worry += worry if m[2] == "old" else int(m[2])
            else:
                worry *= worry if m[2] == "old" else int(m[2])
            worry //= 3
            if worry % m[3]:
                monkeys[m[5]][0].append(worry)
            else:
                monkeys[m[4]][0].append(worry)
        m[0] = []

inspected_max = list(reversed(sorted(inspections)))
print(inspected_max[0] * inspected_max[1])  # 90294
