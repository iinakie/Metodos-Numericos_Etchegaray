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

def f_simple(x):
    # Ejemplo simple: raíz en sqrt(2) ≈ 1.4142...
    return x**2 * math.sin(x) - 1

def df_simple(x):
    return 2*x*math.sin(x) + x**2*math.cos(x)

prueba, iteraciones = newton(f_simple, df_simple, 1.5, 1e-5, 25)
print(f"Raíz aproximada: {prueba}")
print(f"Número de iteraciones: {iteraciones}")

