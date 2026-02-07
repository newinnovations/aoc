#!/usr/bin/env python3


class Axis:
    def __init__(self, a1, a2):
        self.lo = min(a1, a2)
        self.hi = max(a1, a2)

    def overlap(self, a):
        return not (self.hi < a.lo or self.lo > a.hi)

    def __repr__(self):
        if self.lo == self.hi:
            return f"{self.lo}"
        return f"({self.lo}:{self.hi})"


class Shape:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x = Axis(x1, x2)
        self.y = Axis(y1, y2)
        self.z = Axis(z1, z2)

    def drop_to(self, z):
        self.z.hi = z + self.z.hi - self.z.lo
        self.z.lo = z

    def overlaps(self, s):
        return self.x.overlap(s.x) and self.y.overlap(s.y)

    def supports(self, s):
        """Do I (self) support brick (s)"""
        return s.z.lo == self.z.hi + 1 and self.overlaps(s)

    def support(self):
        """Bricks that I (self) support"""
        for i, s in enumerate(bricks):
            if self.supports(s):
                yield i, s

    def num_support(self):
        """Number of bricks that support me (self)"""
        return sum(s.supports(self) for s in bricks)

    def may_disintegrate(self):
        return all(s.num_support() > 1 for _, s in self.support())

    def __repr__(self):
        return f"shape(x={self.x}, y={self.y}, z={self.z})"


def do_drop():
    bricks.sort(key=lambda brick: brick.z.hi)
    for i, brick in enumerate(bricks):
        z = 1
        for b in reversed(bricks[:i]):
            if brick.overlaps(b):
                z = b.z.hi + 1
                break
        brick.drop_to(z)
        bricks.sort(key=lambda brick: brick.z.hi)


bricks = []
with open(0) as f:
    for line in f:
        x1, y1, z1, x2, y2, z2 = map(int, line.strip().replace("~", ",").split(","))
        bricks.append(Shape(x1, y1, z1, x2, y2, z2))

do_drop()

print(sum(brick.may_disintegrate() for brick in bricks))  # 395
