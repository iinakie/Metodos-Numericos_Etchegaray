import math

def biseccion(f, a, b, TOL, N0):
    if f(a) * f(b) > 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None, 0

    i = 1
    FA = f(a)

    while i <= N0:
        p  = a + (b - a)/2.0
        FP = f(p)


        if FP == 0 or (b - a)/2.0 < TOL:
            return p, i

        i = i + 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            # FA no cambia

    print(f"El método fracasó después de N0 iteraciones, N0 = {N0}")
    return None, i-1

def f_simple(x):
    # Ejemplo simple: raíz en sqrt(2) ≈ 1.4142...
    return x**2 * math.sin(x) - 1

prueba, iteraciones = biseccion(f_simple, 1, 2, 1e-5, 25)
print(f"Raíz aproximada: {prueba}")
print(f"Número de iteraciones: {iteraciones}")