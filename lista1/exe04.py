# ---------------------------------------------------------------------------- #
# Em um problema de minimos quadrados, podemos ter situacoes em que 
# algumas variaveis sao mais importante do que as outras. 
# Nesse caso, o problema e chamado de minimos quadrados ponderado, e para resolve-lo, 
# se utiliza o erro ponderado dado por e(x) = W(Ax − b)
# onde W = Diag (w1, w2, · · · , wN ), e wn ∈ R+ e o peso atribuido a cada variavel. 
# Para o problema de minimos quadrados ponderado, encontre o regressor x que minimiza o erro quadratico ponderado.
# ---------------------------------------------------------------------------- #

import numpy as np

def solve_weighted_least_squares(A, b, W):
    x = np.linalg.inv(A.T @ W.T @ W @ A) @ A.T @ W.T @ b
    return x

A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([10, 20, 30])
W = np.diag([2, 1, 2])

regressor_x = solve_weighted_least_squares(A, b, W)

print("Vetor de regressão (x):", regressor_x)