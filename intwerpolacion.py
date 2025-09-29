import numpy as np
"""
def productorio(X, i, x):
    n = len(x)
    res =[(x - X[j]) for j in range(n) if j != i]
    return np.prod(res)

def poli_lagrange(f, X, x):
    n = len(x)
    return sum([f(X[i]) * productorio(X, i, x) / productorio(X, i, X[i]) for i in range(n)])

X = [0, 0.6, 0.9]

def f_A(x):
    return np.cos(x)

def f_B(x):
    return np.sqrt(1 + x)

def f_C(x):
    return np.log(1 + x)

A = poli_lagrange(f_A, X, 0.45)
B = poli_lagrange(f_B, X, 0.45)
C = poli_lagrange(f_C, X, 0.45)

print(f'El valor aproximado de f_A(0.45) es: {A}')
print(f'El valor aproximado de f_B(0.45) es: {B}')
print(f'El valor aproximado de f_C(0.45) es: {C}')

"""

import numpy as np

# ---------- núcleo tipo "tu código" ----------
def productorio(X, i, x):
    n = len(X)                                   # <- ¡ojo! usar X, no x
    res = [(x - X[j]) for j in range(n) if j != i]
    return np.prod(res)

def poli_lagrange_xy(X, Y, x):
    """Interpolante de Lagrange con datos (X,Y) en el punto x."""
    n = len(X)
    términos = []
    for i in range(n):
        num = productorio(X, i, x)
        den = productorio(X, i, X[i])            # Π_{j≠i} (X[i]-X[j])
        términos.append(Y[i] * num / den)
    return float(sum(términos))

# elegir los m+1 nodos más cercanos a x (manteniendo el orden por X)
def subnodos_cercanos(X, Y, x, grado):
    X = np.asarray(X, float); Y = np.asarray(Y, float)
    k = grado + 1
    idx = np.argsort(np.abs(X - x))[:k]
    idx = np.sort(idx)
    return X[idx].tolist(), Y[idx].tolist()

def interp_grado(X, Y, x, grado):
    Xk, Yk = subnodos_cercanos(X, Y, x, grado)
    return poli_lagrange_xy(Xk, Yk, x)

# ---------- Ejercicio 3.2 ----------
# a) f(8.4) con 4 datos
Xa = [8.1, 8.3, 8.6, 8.7]
Ya = [16.94410, 17.56492, 18.50515, 18.82091]
xa = 8.4
Pa1 = interp_grado(Xa, Ya, xa, grado=1)
Pa2 = interp_grado(Xa, Ya, xa, grado=2)
Pa3 = interp_grado(Xa, Ya, xa, grado=3)
print(f"[3.2 a)] f(8.4) ≈ grado1: {Pa1:.8f}, grado2: {Pa2:.8f}, grado3: {Pa3:.8f}")

# b) f(-1/3) con 4 datos
Xb = [-0.75, -0.5, -0.25, 0.0]
Yb = [-0.0718125, -0.02475, 0.33493750, 1.101]
xb = -1.0/3.0
Pb1 = interp_grado(Xb, Yb, xb, grado=1)
Pb2 = interp_grado(Xb, Yb, xb, grado=2)
Pb3 = interp_grado(Xb, Yb, xb, grado=3)
print(f"[3.2 b)] f(-1/3) ≈ grado1: {Pb1:.8f}, grado2: {Pb2:.8f}, grado3: {Pb3:.8f}")

# c) f(0.25) con 4 datos
Xc = [0.1, 0.2, 0.3, 0.4]
Yc = [0.62049958, -0.28398668, 0.00660095, 0.2484244]
xc = 0.25
Pc1 = interp_grado(Xc, Yc, xc, grado=1)
Pc2 = interp_grado(Xc, Yc, xc, grado=2)
Pc3 = interp_grado(Xc, Yc, xc, grado=3)
print(f"[3.2 c)] f(0.25) ≈ grado1: {Pc1:.8f}, grado2: {Pc2:.8f}, grado3: {Pc3:.8f}")
