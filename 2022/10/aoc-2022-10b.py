#!/usr/bin/env python3

program = []
with open(0) as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            program.append(0)
        else:
            program.append(int(line[5:]))

crt = [["."] * 40 for _ in range(6)]


def show_cycle(cycle, x, i):
    global crt
    r, c = (cycle - 1) // 40, (cycle - 1) % 40
    crt[r][c] = "#" if abs(x - c) < 2 else " "


pc, x, cycle = 0, 1, 1
while cycle < 241:
    i = program[pc]
    if i:
        show_cycle(cycle, x, i)
        show_cycle(cycle + 1, x, i)
        x += i
        cycle += 2
    else:
        show_cycle(cycle, x, i)
        cycle += 1
    pc += 1

for row in crt:
    print("".join(row))  # FPGPHFGH

#  #### ###   ##  ###  #  # ####  ##  #  #                                                                                                                   │
#  #    #  # #  # #  # #  # #    #  # #  #                                                                                                                   │
#  ###  #  # #    #  # #### ###  #    ####                                                                                                                   │
#  #    ###  # ## ###  #  # #    # ## #  #                                                                                                                   │
#  #    #    #  # #    #  # #    #  # #  #                                                                                                                   │
#  #    #     ### #    #  # #     ### #  #
