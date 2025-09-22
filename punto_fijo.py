import math

def punto_fijo(g, p0, tol, N):
    """
    Método del punto fijo para encontrar una raíz de la ecuación x = g(x).

    Parámetros: 
    """
    i = 1
    while i <= N:
        p = g(p0)
        if abs(p - p0) < tol:
            return p, i
        i += 1
        p0 = p
    print(f"El método fracasó después de N iteraciones, N = {N}")
    return None, i-1

def g_simple(x):
    # Ejemplo simple: g(x) = (x^2 * sin(x) + 1)^(1/3)
    return math.cos(x)

prueba, iteraciones = punto_fijo(g_simple, 1.5, 1e-5, 1000)
print(f"Raíz aproximada: {prueba}")
print(f"Número de iteraciones: {iteraciones}")