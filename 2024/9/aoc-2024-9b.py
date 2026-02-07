#!/usr/bin/env python3

with open(0) as f:
    line = f.read().strip()

# line = "12345"
# line = "2333133121414131402"

id, isf, line = 0, True, list(map(int, list(line)))

disk2 = list()
len2 = list()
for pos in line:
    if isf:
        disk2 += [id]
        len2 += [pos]
        id += 1
    else:
        disk2 += [-1]
        len2 += [pos]
    isf = not isf

id -= 1

while True:
    pos = disk2.index(id)
    el = len2[pos]
    for p in range(1, pos):
        if disk2[p] == -1 and len2[p] >= el:
            disk2[pos] = -1
            if len2[p] > el:
                if disk2[p + 1] == -1:
                    # disk2[p + 1] = -1
                    len2[p + 1] += len2[p] - el
                    disk2[p] = id
                    len2[p] -= el
                else:
                    disk2[p] = -1
                    len2[p] = len2[p] - el
                    disk2.insert(p, id)
                    len2.insert(p, el)
            else:
                disk2[p] = id
            i = 0
            while i < len(disk2) - 1:
                if disk2[i] == -1 and len2[i] == 0:
                    disk2.pop(i)
                    len2.pop(i)
                else:
                    if disk2[i] == -1 and disk2[i + 1] == -1:
                        len2[i] += len2[i + 1]
                        disk2.pop(i + 1)
                        len2.pop(i + 1)
                    i += 1
            break

    id -= 1
    if id < 0:
        break


total, pos = 0, 0
for i in range(len(disk2)):
    for count in range(len2[i]):
        if disk2[i] != -1:
            total += pos * disk2[i]
        pos += 1

print(total)  # 6436819084274
