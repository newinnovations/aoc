#!/usr/bin/env python3

import re
from ast import literal_eval

p1 = re.compile(r"(\d+|[^\d]+)")


def enumerate_rev(L):
    for index in range(len(L) - 1, -1, -1):
        yield index, L[index]


def add_first(s, a):
    p = p1.findall(s)
    for i, d in enumerate(p):
        if d.isdigit():
            p[i] = str(int(d) + a)
            return "".join(p)
    return s


def add_last(s, a):
    p = p1.findall(s)
    for i, d in enumerate_rev(p):
        if d.isdigit():
            p[i] = str(int(d) + a)
            return "".join(p)
    return s


def explode(s):
    depth = 0
    for i, ch in enumerate(s):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        if depth == 5:
            j = s.index("]", i)
            first, middle, last = (s[:i], s[i + 1 : j], s[j + 1 :])
            a, b = map(int, middle.split(","))
            return add_last(first, a) + "0" + add_first(last, b)
    return None


def split(s):
    p = p1.findall(s)
    for i, d in enumerate(p):
        if d.isdigit():
            n = int(d)
            if n > 9:
                a = n // 2
                b = n - a
                p[i] = add(a, b)
                return "".join(p)
    return None


def add(a, b):
    return f"[{a},{b}]"


def reduce(a):
    if r := explode(a):
        return reduce(r)
    if r := split(a):
        return reduce(r)
    return a


def magnitude(s):
    if isinstance(s, str):
        return magnitude(literal_eval(s))
    elif isinstance(s, int):
        return s
    else:
        return 3 * magnitude(s[0]) + 2 * magnitude(s[1])


assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
assert (
    explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
)
assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

assert split("[[[[0,7],4],[15,[0,13]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
assert (
    split("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
)


a = add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]")
assert reduce(a) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

with open(0) as f:
    lines = [line.strip() for line in f]


a = lines[0]
for b in lines[1:]:
    a = add(a, b)
    a = reduce(a)

print(a)
print(magnitude(a))  # 3051
