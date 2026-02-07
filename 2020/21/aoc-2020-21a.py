#!/usr/bin/env python3

A = dict()
all_ingredients = set()
foods = []
with open(0) as f:
    for line in f:
        line = line.strip().replace(" (contains ", "$").replace(")", "").split("$")
        ingredients = set(line[0].split())
        allergens = line[1].split(", ")
        all_ingredients |= ingredients
        foods.append(ingredients)
        for a in allergens:
            if a in A:
                A[a] = A[a] & ingredients
            else:
                A[a] = ingredients

possible_allergens = set()
for a in A.values():
    possible_allergens |= a
impossible_allergens = all_ingredients - possible_allergens

total = 0
for food in foods:
    for i in food:
        if i in impossible_allergens:
            total += 1

print(total)  # 1815
