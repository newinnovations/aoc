#!/usr/bin/env python3


def seat_id(s):
    row = s[0:7].replace("B", "1").replace("F", "0")
    row = int(row, 2)
    col = s[7:10].replace("R", "1").replace("L", "0")
    col = int(col, 2)
    return row * 8 + col


# print(seat_id("BFFFBBFRRR"))  # row 70, column 7, seat ID 567.
# print(seat_id("FFFBBBFRRR"))  # row 14, column 7, seat ID 119.
# print(seat_id("BBFFBBFRLL"))  # row 102, column 4, seat ID 820.

with open(0) as f:
    ids = [seat_id(line) for line in f]
ids.sort()
# print(ids)

for idx, id in enumerate(ids[:-1]):
    if ids[idx + 1] == id + 2:
        print(id + 1)  # 552
