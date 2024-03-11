# ---------------------------------------------------------------------------- #
# Encontre uma terceira coluna de modo que U seja unitaria. 
# Quanta liberdade ha na coluna 3?
# U =[[1/√3, j/√2, a], [1/√3, 0, b], [j/√3 1/√2 c]]
# ---------------------------------------------------------------------------- #

from sympy import symbols, I, sqrt, Matrix, Eq, solve

a1, b, c = symbols('a1 b c')

U = Matrix([[1/sqrt(3), I/sqrt(2), a1/sqrt(3)],
            [1/sqrt(3), 0, b],
            [I/sqrt(3), 1/sqrt(2), c]])

U_conjugate_transpose = U.H
product = U_conjugate_transpose * U

identity_matrix = Matrix([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]])

equation = Eq(product, identity_matrix)
solutions = solve(equation, (a1, b, c))

print("Resultado:")
print(solutions)
