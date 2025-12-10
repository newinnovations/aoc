#!/usr/bin/env python3

from ortools.sat.python import cp_model


def solve(buttons, target_counters):
    """try to find the number of buttons to press to reach the target (using ortools cp_model)"""

    num_buttons, num_counters = len(buttons), len(target_counters)

    # A button can't be pressed more than the minimal target across the counters it touches
    # because pressing it more would exceed that counter
    upper_bounds = [
        min(target_counters[counter] for counter in but_cntrs) for but_cntrs in buttons
    ]

    model = cp_model.CpModel()
    button_presses = [
        model.NewIntVar(0, upper_bounds[button_nr], f"button_{button_nr}")
        for button_nr in range(num_buttons)
    ]

    # Equality constraints for each counter
    for counter in range(num_counters):
        model.Add(
            sum(
                button_presses[button_nr]
                for button_nr, but_cntrs in enumerate(buttons)
                if counter in but_cntrs
            )
            == target_counters[counter]
        )

    model.Minimize(sum(button_presses))  # objective is to minimize total presses

    solver = cp_model.CpSolver()
    # solver.parameters.max_time_in_seconds = 20
    solution = solver.Solve(model)
    if solution == cp_model.OPTIMAL:  # all solutions have been found
        num_presses = sum([solver.Value(var) for var in button_presses])
        # print(num_presses)
        return num_presses
    print("** failed to solve **")
    return 0


total = 0
with open("input.txt") as f:
    for line in f:
        parts = line.strip().split(" ")
        # buttons indicate which counters each button increments
        buttons = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
        # these are the target values
        target_counters = list(map(int, parts[-1][1:-1].split(",")))
        total += solve(buttons, target_counters)  # number of button presses
print(total)  # 20626
