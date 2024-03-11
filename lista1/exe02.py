# ---------------------------------------------------------------------------- #
# Se w1, w2 e w3 sao vetores independentes, mostre que as somas v1 = w2+w3, v2 = w1+w3 e v3 = w1+w2
# sao linearmente independentes (apresente c1v1 + c2v2 + c3v3 = 0 em termos dos vetores w1, w2 e w3; 
# encontre  e resolva as equacoes para c1, c2 e c3).
# ---------------------------------------------------------------------------- #

import sympy as sp

c1, c2, c3 = sp.symbols('c1 c2 c3')

w1 = sp.MatrixSymbol('w1', 3, 1)
w2 = sp.MatrixSymbol('w2', 3, 1)
w3 = sp.MatrixSymbol('w3', 3, 1)

v1 = w2 + w3
v2 = w1 + w3
v3 = w1 + w2

equation = c1*v1 + c2*v2 + c3*v3

result = sp.solve(sp.Matrix(equation), (c1, c2, c3))

print(f'Coeficientes: {result}')
