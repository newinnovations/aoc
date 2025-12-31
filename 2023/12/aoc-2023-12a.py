#!/usr/bin/env python3

from collections import deque


def count_pos(seq, req):
    q = deque([(seq, 0, req)])
    count = 0
    while q:
        seq, seen_hash, req = q.popleft()
        if not seq:
            ok = (not seen_hash and not req) or (len(req) == 1 and seen_hash == req[0])
            count += ok
        else:
            if seq[0] in ".?":
                if seen_hash:
                    if req and seen_hash == req[0]:
                        q.append((seq[1:], 0, req[1:]))
                else:
                    q.append((seq[1:], 0, req))
            if seq[0] in "#?":
                q.append((seq[1:], seen_hash + 1, req))
    return count


total = 0
with open("input.txt") as f:
    for line in f:
        seq, req = line.strip().split(" ")
        req = list(map(int, req.split(",")))
        count = count_pos(seq, req)
        # print(seq, count)
        total += count
print(total)  # 7674
