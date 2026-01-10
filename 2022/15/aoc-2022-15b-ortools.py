#!/usr/bin/env python3
import re

from ortools.sat.python import cp_model

# Ranges here are [start, finish)  [10,20) and [20,30) touch but do not overlap

with open(0) as f:
    data = [list(map(int, re.findall(r"=([-\d]+)", line.strip()))) for line in f]

MAX = 4000000 if len(data) > 15 else 20

model = cp_model.CpModel()

x = model.new_int_var(0, MAX, "x")
y = model.new_int_var(0, MAX, "y")

ranges = []
for i, (sx, sy, bx, by) in enumerate(data):
    dist = abs(sx - bx) + abs(sy - by)

    diff_x = model.NewIntVar(-MAX, MAX, f"diff_x_{i}")
    diff_y = model.NewIntVar(-MAX, MAX, f"diff_y_{i}")
    model.Add(diff_x == sx - x)
    model.Add(diff_y == sy - y)

    abs_diff_x = model.NewIntVar(0, MAX, f"abs_diff_x_{i}")
    abs_diff_y = model.NewIntVar(0, MAX, f"abs_diff_y_{i}")
    model.AddAbsEquality(abs_diff_x, diff_x)
    model.AddAbsEquality(abs_diff_y, diff_y)

    model.Add(abs_diff_x + abs_diff_y > dist)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    x, y = solver.value(x), solver.value(y)
    print(f"x = {x}")
    print(f"y = {y}")
    print(x * 4000000 + y)  # 13071206703981 (1.4 seconds)
else:
    print("No solution found.")
