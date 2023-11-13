def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")


def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")


def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(abs(int(b))):
            resultado += a
        if b < 0:
            resultado = -resultado
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")


# Ejemplos de uso:
try:
    resultado_suma = sumar(3, 4.5)
    print("Suma:", resultado_suma)
except ValueError as e:
    print(e)

try:
    resultado_resta = restar(8, 2.5)
    print("Resta:", resultado_resta)
except ValueError as e:
    print(e)

try:
    resultado_multiplicacion = multiplicar(2, 3.5)
    print("Multiplicación:", resultado_multiplicacion)
except ValueError as e:
    print(e)
