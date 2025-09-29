import math

def punto_fijo(g, p0, tol, N):
    """
    Método del punto fijo para encontrar una raíz de la ecuación x = g(x).

    Parámetros: 
    """
    i = 0
    while i <= N:
        p = g(p0)
        if abs(p - p0) <= tol:
            return p, i
        i += 1
        p0 = p
    print(f"El método fracasó después de N iteraciones, N = {N}")
    return p0, i-1

def g_A(x):
    # Ejemplo simple: g(x) = (x^2 * sin(x) + 1)^(1/3)
    return (20*x + 21*x**(-2)) / 21

def g_B(x):
    # Otra posible función g(x) para el mismo problema
    if x == 0:
        return float('inf')  # Evitar división por cero 
    return x -((x**3 - 21) / (3*x**2))

def g_C(x):
    # Otra posible función g(x) para el mismo problema
    return x -((x**4 - 21*x) / (x**2 - 21))

def g_D(x):
    # Otra posible función g(x) para el mismo problema
    return (21 / x)**(1/2)

prueba, iteraciones = punto_fijo(g_A, 1, 10**-5, 1)
print(f"\nRaíz aproximada: {prueba}")
print(f"Número de iteraciones: {iteraciones}")
print(f'Error: {abs(prueba**2 - 21**(1/3))}/n')


pruebaB, iteracionesB = punto_fijo(g_B, 1, 10**-5, 1)
print(f"\nRaíz aproximada: {pruebaB}")
print(f"Número de iteraciones: {iteracionesB}")
print(f'Error: {abs(pruebaB**2 - 21**(1/3))}/n')


pruebaC, iteracionesC = punto_fijo(g_C, 1, 10**-5, 1)
print(f"\nRaíz aproximada: {pruebaC}")
print(f"Número de iteraciones: {iteracionesC}")
print(f'Error: {abs(pruebaC**2 - 21**(1/3))}/n')

pruebaD, iteracionesD = punto_fijo(g_D, 1, 10**-5, 1)
print(f"\nRaíz aproximada: {pruebaD}")    
print(f"Número de iteraciones: {iteracionesD}")
print(f'Error: {abs(pruebaD**2 - 21**(1/3))}/n')
