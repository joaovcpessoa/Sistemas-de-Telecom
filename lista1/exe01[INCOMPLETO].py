# ---------------------------------------------------------------------------- #
# Verdadeiro ou falso para M ∈ R3×3 (verifique a soma utilizando um exemplo)?
# a) As matrizes antissimetricas de M formam um subespaco de R3×3?
# b) As matrizes assim´etricas de M formam um subespaco
# c) As matrizes que possuem [1 1 1]T em seu espaco nulo formam um subespaco
# Matriz antissimetrica: A^T = −A
# Matriz assimetrica: A^T != −A
# Condicoes para ser um subspaco:
# - elemento nulo
# - operação de adicao fechada
# - operação de multiplicacao fechada
# ---------------------------------------------------------------------------- #

import numpy as np

A = np.array([[0, 1, -1],
              [-1, 0, 2],
              [1, -2, 0]])

B = np.array([[0, -2, 1],
              [2, 0, -1],
              [-1, 1, 0]])

# a) Verificando se a soma de matrizes antissimétricas é novamente antissimétrica
sum_matrix = A + B
is_antissymmetric_sum = np.allclose(sum_matrix, -sum_matrix.T)
print("a) A soma de matrizes antissimétricas é antissimétrica:", is_antissymmetric_sum)

# b) Verificando que matrizes assimétricas não formam um subespaço
asymmetric_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
sum_asymmetric = A + asymmetric_matrix
is_asymmetric_sum = not np.allclose(sum_asymmetric, -sum_asymmetric.T)
print("b) Matrizes assimétricas não formam um subespaço:", is_asymmetric_sum)

# c) Verificando que matrizes com [1 1 1]^T no espaço nulo não formam um subespaço
matrix_with_ones = np.array([[1, 1, 1],
                             [0, 0, 0],
                             [0, 0, 0]])
null_space_test = np.allclose(np.dot(A, matrix_with_ones), np.zeros((3, 1)))
print("c) Matrizes com [1 1 1]^T no espaço nulo não formam um subespaço:", not null_space_test)

