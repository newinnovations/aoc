#!/usr/bin/env python3

from functools import cache


@cache
def present_size(present_idx):
    shape = shapes[present_idx]
    return len(shape) * len(shape[0])
    # return sum(x == "#" for row in shapes[present_idx] for x in row)


def enough_space_available(width, height, present_counts):
    area_size = width * height
    total_needed = sum(
        count * present_size(present_idx)
        for present_idx, count in enumerate(present_counts)
    )
    return area_size >= total_needed


idx = -1
shapes = dict()
presents = list()
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line.endswith(":"):
            idx = int(line[:-1])
            shapes[idx] = list()
        elif "." in line or "#" in line:
            shapes[idx].append(list(line))
        elif ":" in line:
            s = line.split(": ")
            width, height = map(int, s[0].split("x"))
            present_counts = list(map(int, s[1].split(" ")))
            presents.append((width, height, present_counts))

# Day 12 can just be solved by checking basic space requirements.
# Complex rotating and fitting is just not needed. A joke or a pity?
#
# If you look closely at the few shapes inside the input data, you can see
# or feel that there is (almost?) no possibility for shapes to share space.
#
# I changed the size calculation of the present shape to better fit the
# idea that space cannot be shared, so we need to look at width and height
# of the shape instead of the number of "#". Did not change the outcome.
#
# NOTE: this solution does not work with the sample data
print(
    sum(
        enough_space_available(w, h, present_counts)
        for w, h, present_counts in presents
    )
)  # 526
