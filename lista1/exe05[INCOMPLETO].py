# ---------------------------------------------------------------------------- #
# Sendo ortonormais os vetores q1, q2 e q3, qual combinacao de q1 e q2 esta mais proxima de q3?
# Minimizar ∣∣q3−c1*q1−c2*q2∣∣^2
# ---------------------------------------------------------------------------- #

import sympy as sp

c1, c2 = sp.symbols('c1 c2')

q1 = sp.Matrix([1/sp.sqrt(2), 1/sp.sqrt(2), 0])
q2 = sp.Matrix([-1/sp.sqrt(2), 1/sp.sqrt(2), 0])
q3 = sp.Matrix([0, 0, 1])

objective = sp.sqrt((q3 - c1*q1 - c2*q2).dot(q3 - c1*q1 - c2*q2))

result = sp.solve([sp.diff(objective, c1), sp.diff(objective, c2)], (c1, c2))

print(f'Combinacao linear: {result}')