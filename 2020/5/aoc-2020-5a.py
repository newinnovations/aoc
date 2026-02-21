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

max_id = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        id = seat_id(line)
        if id > max_id:
            max_id = id

print(max_id)  # 855
