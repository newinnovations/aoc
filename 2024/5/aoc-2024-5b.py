#!/usr/bin/env python3

total, rules, updates = 0, dict(), list()
with open(0) as f:
    for line in f:
        if "|" in line:
            a, b = map(int, line.strip().split("|"))
            if a not in rules:
                rules[a] = []
            rules[a].append(b)
        elif "," in line:
            updates.append(list(map(int, line.strip().split(","))))

for update in updates:
    ok = True
    for i in range(len(update)):
        rule = rules.get(update[i], [])
        for page in update[:i]:
            if page in rule:
                ok = False

    if ok:
        continue

    corrected = list()
    for value in update:
        rule = rules.get(value, [])
        pos = len(corrected)
        for idx in reversed(range(len(corrected))):
            if corrected[idx] in rule:
                pos = idx
        corrected.insert(pos, value)

    total += corrected[len(corrected) // 2]

print(total)  # 4655
