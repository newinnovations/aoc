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

with open(0) as f:
    passports = f.read().split("\n\n")
    passports = [g.split() for g in passports]

# print(passports)

total = 0
for passport in passports:
    fields = set(f.split(":")[0] for f in passport)
    fields.add("cid")
    total += fields == FIELDS

print(total)  # 213
