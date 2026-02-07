#!/usr/bin/env python3

A = dict()
with open(0) as f:
    for line in f:
        line = line.strip().replace(" (contains ", "$").replace(")", "").split("$")
        ingredients = set(line[0].split())
        allergens = line[1].split(", ")
        for a in allergens:
            if a in A:
                A[a] = A[a] & ingredients
            else:
                A[a] = ingredients

mapping = dict()
while A:
    for i, a in A.items():
        if len(a) == 1:
            mapping[i] = a.pop()
    for a in mapping.keys():
        if a in A:
            del A[a]
    for i in mapping.values():
        for a in A.keys():
            A[a].discard(i)

allergens = sorted(mapping.keys())
ingredients = [mapping[a] for a in allergens]
print(",".join(ingredients))  # kllgt,jrnqx,ljvx,zxstb,gnbxs,mhtc,hfdxb,hbfnkq
