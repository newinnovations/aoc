#!/usr/bin/env python3

from collections import defaultdict

files = defaultdict(int)

pwd = []
total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        if line.startswith("$ cd "):
            dir = line[5:]
            if dir == "/":
                pwd = ["/"]
            elif dir == "..":
                pwd = pwd[:-1]
            else:
                pwd.append(dir)
        if not (line.startswith("$ ") or line.startswith("dir ")):
            for i in range(len(pwd)):
                files[tuple(pwd[: i + 1])] += int(line.split(" ")[0])

for _, size in files.items():
    if size < 100000:
        total += size
print(total)  # 1449447
