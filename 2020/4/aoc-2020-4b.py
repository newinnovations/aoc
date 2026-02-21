#!/usr/bin/env python3

FIELDS = {
    "byr",  # Birth Year
    "iyr",  # Issue Year
    "eyr",  # Expiration Year
    "hgt",  # Height
    "hcl",  # Hair Color
    "ecl",  # Eye Color
    "pid",  # Passport ID
    "cid",  # Country ID
}

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

with open(0) as field:
    passports = field.read().split("\n\n")
    passports = [g.split() for g in passports]

# print(passports)

total = 0
for passport in passports:
    fields = set(f.split(":")[0] for f in passport)
    fields.add("cid")
    if fields != FIELDS:
        continue

    for fields in passport:
        field, value = fields.split(":")
        if field == "hcl":
            if (
                len(value) != 7
                or value[0] != "#"
                or not all("0" <= ch <= "9" or "a" <= ch <= "f" for ch in value[1:])
            ):
                break
        elif field == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                break
        elif field == "pid":
            if len(value) != 9 or not all("0" <= ch <= "9" for ch in value):
                break
        elif field == "byr":
            value = int(value)
            if value < 1920 or value > 2002:
                break
        elif field == "iyr":
            value = int(value)
            if value < 2010 or value > 2020:
                break
        elif field == "eyr":
            value = int(value)
            if value < 2020 or value > 2030:
                break
        elif field == "hgt":
            if value.endswith("in"):
                value = int(value[:-2])
                if value < 59 or value > 76:
                    break
            elif value.endswith("cm"):
                value = int(value[:-2])
                if value < 150 or value > 193:
                    break
            else:
                break
    else:
        total += 1

print(total)  # 147
