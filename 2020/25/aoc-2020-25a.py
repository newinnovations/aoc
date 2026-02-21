#!/usr/bin/env python3

with open(0) as f:
    public_keys = list(map(int, (line for line in f.read().splitlines())))


def inv_calc(subject_number, target_value):
    current_value = 1
    for loop_size in range(1, 20201227):
        current_value = (current_value * subject_number) % 20201227
        if current_value == target_value:
            return loop_size


def calc(subject_number, loop_size):
    return pow(subject_number, loop_size, 20201227)


loop_sizes = [inv_calc(7, pk) for pk in public_keys]

# The card transforms the subject number of the door's public key according to the card's loop size.
# The result is the encryption key.

key0 = calc(public_keys[1], loop_sizes[0])

# The door transforms the subject number of the card's public key according to the door's loop size.
# The result is the same encryption key as the card calculated.

key1 = calc(public_keys[0], loop_sizes[1])

assert key0 == key1

print(key0)  # 3803729
