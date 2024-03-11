import numpy as np

V = np.array([[-1, 3], [1, 3]])
Lambda = np.array([[-0.5, 0.5], [0.5, 0.5]])

product_V_Lambda = np.dot(V, Lambda)

print("Produto de V por Lambda:")
print(product_V_Lambda)