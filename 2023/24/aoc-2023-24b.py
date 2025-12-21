#!/usr/bin/env python3

from sympy import Matrix


def plucker(px, py, pz, vx, vy, vz):
    d = Matrix([vx, vy, vz])
    m = Matrix([px, py, pz]).cross(d)
    return d, m


# def plucker_inverse(d, m):
#     p = d.cross(m)
#     return p, d


def plucker_intersection_point(d1, m1, d2, m2):
    # Assume that lines do indeed intersect and are not parallel.
    def skew(d):
        # Skew-symmetric matrix S(d) such that S(d) * p = d × p.
        dx, dy, dz = d
        return Matrix([[0, -dz, dy], [dz, 0, -dx], [-dy, dx, 0]])

    # From p × d = m  ⇒  -skew(d) * p = m
    A = Matrix.vstack(-skew(d1), -skew(d2))  # 6x3
    b = Matrix.vstack(m1, m2)  # 6x1
    # Solve (A^T A) p = A^T b  (unique solution since lines intersect & not parallel)
    p = (A.T * A).LUsolve(A.T * b)
    return p


def time_and_intersection(stone, d_sol, m_sol):
    px, py, pz, vx, vy, vz = stone
    d, m = plucker(px, py, pz, vx, vy, vz)
    point = plucker_intersection_point(d, m, d_sol, m_sol)
    t = (point[0] - px) / vx
    return t, point


STONES = []
with open("input.txt") as f:
    for line in f:
        px, py, pz, vx, vy, vz = map(
            int, line.strip().replace(" ", "").replace("@", ",").split(",")
        )
        STONES.append((px, py, pz, vx, vy, vz))

# Transform to Plücker coordinates (5 stones are enough to obtain the solution)
A = []
for s in STONES[:5]:
    d, m = plucker(*s)
    A.append(d[:] + m[:])

# Find the intersecting line by determining nullspace/kernel of A
M = Matrix(A)
ker = M.nullspace()
assert len(ker) == 1

# Extract Plücker coordinates of the intersecting line
d_sol = Matrix(ker[0][3:])
m_sol = Matrix(ker[0][:3])

# Find starting point (position on t=0)
t1, p1 = time_and_intersection(STONES[0], d_sol, m_sol)
t2, p2 = time_and_intersection(STONES[1], d_sol, m_sol)
start = p1 - t1 * ((p2 - p1) / (t2 - t1))

# Sum x, y and z
print(sum(start))
