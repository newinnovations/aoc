#!/usr/bin/env python3

from functools import cache


def count_possibilities(seq, req):
    @cache
    def count_recursive(seq, req, seen_hash):  # always len(req) > 0
        if not seq:
            return len(req) == 1 and seen_hash == req[0]
        count = 0
        if seq[0] in ".?":
            if seen_hash:
                if seen_hash == req[0]:  # return because ? cannot be #
                    if len(req) == 1:
                        return "#" not in seq
                    return count_recursive(seq[1:], tuple(req[1:]), 0)
            elif len(seq) >= sum(req) + len(req):
                count += count_recursive(seq[1:], req, 0)
        if seq[0] in "#?" and seen_hash < req[0]:
            count += count_recursive(seq[1:], req, seen_hash + 1)
        return count

    return count_recursive(seq, req, 0)


total = 0
with open("input.txt") as f:
    for line in f:
        seq, req = line.strip().split(" ")
        req = tuple(map(int, req.split(",")))
        seq = "?".join([seq] * 5)
        req = tuple(req * 5)
        count = count_possibilities(seq, req)
        # print(seq, count)
        total += count
print(total)  # 4443895258186
