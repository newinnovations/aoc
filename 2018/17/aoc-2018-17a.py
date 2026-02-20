#!/usr/bin/env python3

from re import compile


def dump():
    for y in range(min_y - 1, max_y + 2):
        print(f"{y:4}", end=": ")
        for x in range(min_x - 3, max_x + 2):
            if (x, y) in clay:
                if (x, y) in water:
                    print("~", end="")
                else:
                    print("#", end="")
            else:
                if (x, y) in water:
                    print("|", end="")
                else:
                    print(".", end="")
        print()
    print()


def pour_once(x, y):
    """Pour water once at (x,y)
    Returns whether we must run again
    - `True` if we filled an enclosed area with water,
    - `False` if water escapes at the bottom
    """

    while y <= max_y and (x, y) not in clay:
        if y >= min_y:
            water.add((x, y))
        y += 1

    if y > max_y:
        # Water drips away at the bottom
        return False

    # At `y` we have clay or water

    y -= 1

    # Now `y` is the layer above. Check if it is enclosed and can contain water
    # or is open and spills water to the left, right or both.
    x_left = x_right = x
    left_spill = right_spill = None

    while not (x_left, y) in clay:
        water.add((x_left, y))
        if not (x_left, y + 1) in clay:
            left_spill = x_left
            break
        x_left -= 1

    while not (x_right, y) in clay:
        water.add((x_right, y))
        if not (x_right, y + 1) in clay:
            right_spill = x_right
            break
        x_right += 1

    if left_spill is None and right_spill is None:
        # Water is contained. Add "still" water in enclosed area as "clay"
        # because it behaves in the same way as existing clay for additional
        # water
        clay.update([(i, y) for i in range(x_left + 1, x_right)])
        return True

    # Water cannot be contained as it spills left, right or both
    must_run_again = False
    if left_spill is not None:
        must_run_again = must_run_again or pour(left_spill, y + 1)
    if right_spill is not None:
        must_run_again = must_run_again or pour(right_spill, y + 1)
    return must_run_again


def pour(x, y):
    """Keep pouring water at (x, y) until water has either reached (x, y) or
    we have filled enclosed areas below and all water now escapes at the bottom.

    If water has reached (x,y) the situation may have changed for the upper level
    `pour` and it must be run again.

    Returns `True` if water has reached (x, y), `False` if water escapes at the bottom.
    """
    if (x, y) in done:
        return False
    done.add((x, y))
    while pour_once(x, y):
        if (x, y) in clay:
            return True
    return False


pattern = compile(r"(.)=(\d+), .=(\d+)\.\.(\d+)")

water = set()
done = set()
clay = set()
with open(0) as f:
    for line in f:
        line = line.strip()
        a, b, c, d = pattern.findall(line)[0]
        b, c, d = int(b), int(c), int(d)
        for i in range(c, d + 1):
            if a == "x":
                clay.add((b, i))
            else:
                clay.add((i, b))

xvals, yvals = zip(*clay)
min_x, max_x = min(xvals), max(xvals)
min_y, max_y = min(yvals), max(yvals)

pour(500, 0)

dump()

print("A", len(water))  # 31788
print("B", len(clay & water))  # 25800
