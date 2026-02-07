#!/usr/bin/env python3

from sympy import Eq, solve, symbols

particles = []
with open("input.txt") as f:
    for line in f:
        par_px, par_py, par_pz, par_vx, par_vy, par_vz = map(
            int, line.strip().replace(" ", "").replace("@", ",").split(",")
        )
        particles.append((par_px, par_py, par_pz, par_vx, par_vy, par_vz))

px, py, pz = symbols("px"), symbols("py"), symbols("pz")
vx, vy, vz = symbols("vx"), symbols("vy"), symbols("vz")
t = []
constraints = []
for i, (par_px, par_py, par_pz, par_vx, par_vy, par_vz) in enumerate(particles[:3]):
    t.append(symbols(f"t{i}"))
    constraints.append(Eq(px + vx * t[i], par_px + par_vx * t[i]))
    constraints.append(Eq(py + vy * t[i], par_py + par_vy * t[i]))
    constraints.append(Eq(pz + vz * t[i], par_pz + par_vz * t[i]))
sol = solve(constraints)[0]
print(sol[px] + sol[py] + sol[pz])  # 856642398547748
