# ---------------------------------------------------------------------------- #
# Os autovalores de A sao 1 e 9, os de B sao −1 e 9:
# A = [[5 4],[4 5]] e B = [[4 5],[5 4]]
# Encontre uma raiz quadrada matricial de A a partir de R = V*sqrt(Λ)V^−1 
# Porque nao existe raiz quadrada matricial real de B?
# ---------------------------------------------------------------------------- #

import numpy as np

A = np.array([[5, 4], [4, 5]])

eigenvalues, eigenvectors = np.linalg.eig(A)
Lambda = np.diag(np.sqrt(eigenvalues))
R = np.dot(np.dot(eigenvectors, Lambda), np.linalg.inv(eigenvectors))

print("Matriz R:")
print(R)

# B) Isso ocorre porque a matriz B possui um autovalor negativo, ou seja, 
# matriz não é definida positiva, e, portanto, não tem uma raiz quadrada matricial real. 
