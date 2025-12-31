#!/usr/bin/env python3


def hash(s):
    val = 0
    for ch in s:
        val += ord(ch)
        val *= 17
        val %= 256
    return val


with open("input.txt") as f:
    steps = f.read().strip().split(",")

boxes = {id: [] for id in range(256)}

for s in steps:
    # print(s)
    if s[-1] == "-":
        # go to the relevant box and remove the lens with the given label if it is present in the box.
        # move any remaining lenses as far forward in the box as they can go without changing their order
        # filling any space made by removing the indicated lens.
        label = s[:-1]
        box = boxes[hash(label)]
        for slotno, lens in enumerate(box):
            if lens[0] == label:
                del box[slotno]
                break
    else:
        label, fl = s.split("=")
        # if there is already a lens in the box with the same label, replace the old lens
        # otherwise add the lens to the box immediately behind any lenses already in the box
        box = boxes[hash(label)]
        for slotno, lens in enumerate(box):
            if lens[0] == label:
                box[slotno] = (label, int(fl))
                break
        else:
            box.append((label, int(fl)))

total = 0
for boxno in range(256):
    for slotno, (label, fl) in enumerate(boxes[boxno]):
        total += (boxno + 1) * (slotno + 1) * fl
print(total)  # 251353
