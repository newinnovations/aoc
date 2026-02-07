#!/usr/bin/env python3

with open(0) as f:
    line = f.read().strip()

# line = "12345"
# line = "2333133121414131402"

id, isf, line = 0, True, list(map(int, list(line)))

disk = list()
for n in line:
    if isf:
        disk += [id] * n
        id += 1
    else:
        disk += [-1] * n
    isf = not isf

front, end = 0, len(disk) - 1
while front < end:
    if disk[front] != -1:
        front += 1
    elif disk[end] == -1:
        end -= 1
    else:
        disk[front] = disk[end]
        disk[end] = -1
        front += 1
        end -= 1

total = 0
for n, id in enumerate(disk):
    if id != -1:
        total += n * id

print(total)  # 6415184586041
