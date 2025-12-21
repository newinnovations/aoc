# Advent of Code 2023, Day 24

## Plücker coordinates

For a particle with initial position $\mathbf{p}=(p_{x},p_{y},p_{z})$ and velocity $\mathbf{v}=(v_{x},v_{y},v_{z})$, the Plücker coordinates $(\mathbf{d}:\mathbf{m})$ are derived as follows:

- Direction Vector ($\mathbf{d}$): This is simply the velocity vector of the particle, which determines the orientation of the line.\
  $\mathbf{d}=\mathbf{v}=(v_{x},v_{y},v_{z})$

- Moment Vector ($\mathbf{m}$): This is the cross product of the position vector and the velocity vector. It represents the perpendicular distance from the origin to the line, scaled by the magnitude of the velocity.\
  $\mathbf{m}=\mathbf{p}\times \mathbf{v}=(p_{y}v_{z}-p_{z}v_{y},p_{z}v_{x}-p_{x}v_{z},p_{x}v_{y}-p_{y}v_{x})$

The line is represented by the 6-tuple: $\mathcal{L}=(v_{x},v_{y},v_{z},m_{x},m_{y},m_{z})$

## Key Properties of Plücker coordinates

- Time Independence: Although the particle moves over time $t$, the Plücker coordinates remain constant.
  Replacing $\mathbf{p}$ with any point on the path $\mathbf{r}(t)=\mathbf{p}+\mathbf{v}t$ yields the same moment vector
  because $(\mathbf{p}+\mathbf{v}t)\times \mathbf{v}=\mathbf{p}\times \mathbf{v}+t(\mathbf{v}\times \mathbf{v})$, and $\mathbf{v}\times \mathbf{v}=0$.

- Orthogonality: By definition, the direction and moment vectors are always orthogonal: $\mathbf{d}\cdot \mathbf{m}=0$.

- Homogeneity: Plücker coordinates are often treated as homogeneous coordinates in projective space $\mathbb{P}^{5}$; scaling the entire 6-tuple by a non-zero constant describes the same geometric line.

## Approach

If you suspect a **true transversal** exists (intersects every line), this is the cleanest, most principled approach.

**Key idea:** A 3D line can be represented by Plücker coordinates $(\mathbf{d}:\mathbf{m})$, where:

- $\mathbf{d}$ is the direction vector of the line (non-zero).
- $\mathbf{m} = \mathbf{p} \times \mathbf{d}$ is the moment.
- They satisfy the **Plücker relation** $\mathbf{d} \cdot \mathbf{m} = 0$.

A line $(\mathbf{d}:\mathbf{m})$ intersects a given line $(\mathbf{d}_n, \mathbf{m}_n=\mathbf{p}_n \times \mathbf{d}_n)$ **iff**:

$$
\mathbf{d}\cdot\mathbf{m}_n + \mathbf{d}_n\cdot\mathbf{m} = 0.
$$

This is **linear** in the 6 unknowns $[\mathbf{d}; \mathbf{m}]$. Stack these for all (n) to get a linear system:

$$
A \begin{bmatrix} \mathbf{d} \\ \mathbf{m} \end{bmatrix} = 0, \quad \text{and enforce } \mathbf{d}\cdot\mathbf{m}=0 \text{ (quadratic constraint)}.
$$

**Algorithm sketch:**

1. Build $A\in\mathbb{R}^{N\times 6}$ with each row $[m_{n,x}, m_{n,y}, m_{n,z}, d_{n,x}, d_{n,y}, d_{n,z}]$.
2. Find the intersecting line by determining **nullspace** of $A$.
3. Use intersection points and corresponding times on two lines to determine the position on $t=0$

## Nullspace or kernel of a matrix

In linear algebra, the nullspace (also called the kernel) of a matrix $A$ is the set of all vectors $\mathbf{x}$ that,
when multiplied by $A$, result in the zero vector ($\mathbf{0}$).

Mathematically, it is defined as: $$\text{ker}(A)=\{\mathbf{x}\mid A\mathbf{x}=\mathbf{0}\}$$

### Key Concepts

- **"Killed" Vectors**: Visually, if you think of a matrix as a machine that transforms space, the nullspace consists of all the input vectors that the machine "squashes" down to the origin (zero).

- **Subspace Properties**: The nullspace is always a valid subspace of the input space ($\mathbb{R}^{n}$). This means it contains the zero vector and is closed under addition and scalar multiplication.

- **Nullity**: The dimension of the nullspace—the number of linearly independent vectors needed to span it—is called the nullity of the matrix.

### Why it Matters

- **Solving Equations**: The nullspace describes all solutions to the homogeneous system $A\mathbf{x}=\mathbf{0}$.

## Find intersection point of two lines given in Plücker coordinates

Assume the lines intersect and are not parallel, so we can solve directly. For each line, the Plücker relation is:

$$
\mathbf{p} \times \mathbf{d} = \mathbf{m} \quad \Longleftrightarrow \quad -[\mathbf{d}]_\times \mathbf{p} = \mathbf{m}
$$

where $[\mathbf{d}]_\times$ is the **$3\times3$** skew-symmetric matrix that implements the cross product.
Stacking the two lines gives a **$6\times3$** linear system in $\mathbf{p}$.
Since the lines intersect, the system is consistent and we can get $\mathbf{p}$ via normal equations.
