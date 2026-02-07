#!/usr/bin/env python3


def apply_single_mapping(mapping, id):
    for dst, src, rng in mapping:
        if id >= src and id < src + rng:
            return dst + id - src
    return id


def aplly_all_mappings(id):
    for mapping in mappings:
        id = apply_single_mapping(mapping, id)
    return id


seeds, mappings, mapping = [], [], []
with open(0) as f:
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

print(min(aplly_all_mappings(seed) for seed in seeds))  # 88151870
