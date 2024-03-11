# ---------------------------------------------------------------------------- #
# Prove que A^H*A é sempre uma matriz hermitiana.
# Calcule A^H*A e A*A^H: A = [[j 1 j],[1 j j]]
# ---------------------------------------------------------------------------- #

import numpy as np

A = np.array([[1j, 1, 1j], [1, 1j, 1j]])

AH = np.conj(A.T)
result_AHA = np.dot(AH, A)
print('A^H * A:')
print(result_AHA)

is_hermitian = np.allclose(result_AHA, result_AHA.T.conj())
print(f'\nCondicao: {is_hermitian}')
