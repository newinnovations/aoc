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
        content = [c.split(" ", 1)[1] for c in content]
        bags[key] = content

bag_set = set()
go_on = True
while go_on:
    go_on = False
    for k, v in bags.items():
        if k in bag_set:
            continue
        if "shiny gold" in v:
            go_on = True
            bag_set.add(k)
        else:
            for r in bag_set:
                if r in v:
                    go_on = True
                    bag_set.add(k)
                    break

print(len(bag_set))  # 164
