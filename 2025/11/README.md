# Advent of Code 2025, Day 11

Day 11 featured the most most interesting puzzle this year.

The fist part can be solved with a very simple recursive path counting algorithm.

The second part is similar but has a much a larger graph and two nodes that need to be
part of the path. I tried several approaches, one of which I really like as it is
minimalistic and easy to read. I also tried solving it bottom up, like day 7. It works
but it requires sorting the graph first (Kahn's algortihm) and several counters with
each node.

## Files

- `aoc-2025-11a.py`: first puzzle with recursive path counting
- `aoc-2025-11b.py`: second puzzle with the optimal (recursive) solution
- `aoc-2025-11b-sub-paths.py`: second puzzle using the sub paths approach
- `aoc-2025-11b-reverse.py`: solving from the bottom up, more complex than expected
