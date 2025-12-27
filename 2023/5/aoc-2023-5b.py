#!/usr/bin/env python3


def aplly_all_mappings(ranges):
    """Apply all mappings to a list of ranges"""
    for mapping in mappings:
        ranges = apply_mapping(mapping, ranges)
    return ranges


def apply_mapping(mapping, ranges):
    """Apply single mapping (list of rules) to a list of ranges"""
    result = []
    for dst, src, length in mapping:
        untouched_ranges = []
        for r in ranges:
            t, ut = apply_rule(r, dst, src, length)
            result += t
            untouched_ranges += ut
        ranges = untouched_ranges
    result += ranges
    return compact_ranges(result)


def apply_rule(range, dst, src, length):
    """Apply single rule (dst, src, length) to a single range [start, finish)

    Returns two range lists. One contains ranges (0 or 1) touched by this rule,
    which do not need to be processed further. The second contains ranges (0, 1 or 2)
    that are not touched by this rule and need to be processed further as they
    may be touched by following rules.

    touched, untouched       rrrrrrrr
          0, 1           --  |      |
          1, 1           ---------- |
          1, 2           -----------------
          1, 0               | ---- |
          1, 1               | -----------
          0, 1               |      |  ---

    """
    range_s, range_f = range
    rule_s = src
    rule_f = src + length

    result_touched = []
    result_untouched = []

    f = min(range_f, rule_s)
    if f > range_s:  # part before is untouched
        result_untouched.append((range_s, f))

    s = max(range_s, rule_s)
    f = min(range_f, rule_f)
    if f > s:  # overlap: touched
        result_touched.append((s + dst - src, f + dst - src))

    s = max(range_s, rule_f)
    if range_f > s:  # part after is untouched
        result_untouched.append((s, range_f))

    return result_touched, result_untouched


def combine_two_ranges(a, b):
    """Combines two ranges to one or returns None if they cannot be combined

           bbbbbbbb
    1  aa  |      |
    2  aaaa|      |
    3  aaaaaaaaaa |
    4  aaaaaaaaaaaaaaaa
    5      | aaaa |
    6      | aaaaaaaaaa
    7      |      |aaaa
    8      |      |  aa

    """
    (a_s, a_f), (b_s, b_f) = a, b

    if a_s > b_f or b_s > a_f:  # no overlap/touch (1, 8)
        return None

    # b inside a (4), a inside b (5), overlap (3, 6) or touch (2, 7)
    return (min(a_s, b_s), max(a_f, b_f))


def compact_ranges(ranges):
    result, cur = [], None
    for range in sorted(ranges):
        if cur is None:
            cur = range
        else:
            combined = combine_two_ranges(cur, range)
            if combined is None:
                result.append(cur)
                cur = range
            else:
                cur = combined
    if cur is not None:
        result.append(cur)
    return result


seeds, mappings, mapping = [], [], []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            if "seeds:" in line:
                seeds = list(map(int, line[7:].split(" ")))
            elif "map:" in line:
                if mapping:
                    mappings.append(mapping)
                    mapping = []
            else:
                mapping.append(tuple(map(int, line.split(" "))))
mappings.append(mapping)

# In math square brackets [] mean an endpoint is included (closed), while round brackets ()
# mean it's excluded (open); so [2, 5] is 2, 3, 4, 5 (inclusive), but (2, 5) is 3, 4
# (exclusive), with mixed brackets like [2, 5) including 2 but not 5.
#
# Ranges here are [start, finish)  [10,20) and [20,30) touch but do not overlap
seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

print(aplly_all_mappings(seed_ranges)[0][0])  # 2008785
