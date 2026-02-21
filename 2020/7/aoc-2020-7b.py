#!/usr/bin/env python3

bags = dict()
with open(0) as f:
    for line in f:
        line = line.strip()
        key, content = line.split(" bags contain ")
        content = content.replace(" bags", "").replace(" bag", "").replace(".", "")
        if content == "no other":
            content = []
        elif ", " in content:
            content = content.split(", ")
        else:
            content = [content]
        content = [(c.split(" ", 1)[1], int(c.split(" ", 1)[0])) for c in content]
        bags[key] = content


def total_bags(color):
    res = 1
    for col, count in bags[color]:
        res += count * total_bags(col)
    return res


print(total_bags("shiny gold") - 1)  # 7872
