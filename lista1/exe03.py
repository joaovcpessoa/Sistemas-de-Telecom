# ---------------------------------------------------------------------------- #
# Encontre o x que minimize o erro quadratico do sistema
# Qual a projecao de b no espaco coluna de A?
# ---------------------------------------------------------------------------- #

import numpy as np

A = np.array([[1, -1], [1, 0], [1, 1]])
b = np.array([[4], [5], [9]])

# x = np.linalg.lstsq(A, b, rcond=None)[0]
x = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), b)
p = np.dot(A, x)

print(f'Vetor: {x}')
print(f'Projecao: {p}')