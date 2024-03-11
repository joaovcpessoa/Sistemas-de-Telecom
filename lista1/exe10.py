# ---------------------------------------------------------------------------- #
# Diagonalize as seguintes matrizes, construindo as matrizes Λ e V:
# a) A = [[2 1-j],[1+j 3]]
# b) V = 1/sqrt(3) * [[1 1-j],[1+j -1]]
# ---------------------------------------------------------------------------- #

import numpy as np

A = np.array([[2, 1j-1], [1j+1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)
Lambda = np.diag(eigenvalues)
V = eigenvectors

np.set_printoptions(precision=3, suppress=True)

print("Matriz Lambda:")
print(Lambda)
print("\nMatriz V:")
print(V)
