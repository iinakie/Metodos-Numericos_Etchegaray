import math

def newton(f, df, p0, tol, N):
    i = 1
    while i <= N:
        p = p0 - f(p0)/df(p0)
        if abs(p - p0) < tol:
            return p, i
        i += 1
        p0 = p
    print(f"El método fracasó después de N iteraciones, N = {N}")
    return None, i-1

def f(x):
    # Ejemplo simple: raíz en sqrt(2) ≈ 1.4142...
    return 1000/x * (1 - (1 + x)**-360) -135000

def df_simple(x):
    return -1000/x**2 * (1 - (1 + x)**-360) + 360000 * (1 + x)**-361

prueba, iteraciones = newton(f, df_simple, 0.0005, 10**-5, 10000)
print(f"Raíz aproximada: {prueba}")
print(f"Número de iteraciones: {iteraciones}")

