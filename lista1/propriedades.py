import numpy as np

V = np.array([[1j, 1, 1j], [1, 1j, 1j]])
V_pinv = np.linalg.pinv(V)

# Transpose of the matrix
V_transposta = V.T
V_H = np.conj(V.T)

print("Pseudo-Inverse of V:")
print(V_pinv)

print("\nTranspose of Matrix V:")
print(V_transposta)

print("\nHermitian of Matrix V:")
print(V_H)