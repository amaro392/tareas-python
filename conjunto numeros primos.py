def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generar_primos(rango_inicio, rango_fin):
    """Genera un conjunto de números primos dentro de un rango específico."""
    primos = set()
    for numero in range(rango_inicio, rango_fin + 1):
        if es_primo(numero):
            primos.add(numero)
    return primos

# Solicitar al usuario el rango
rango_inicio = int(input("Introduce el inicio del rango: "))
rango_fin = int(input("Introduce el fin del rango: "))

# Generar el conjunto de números primos
primos = generar_primos(rango_inicio, rango_fin)

# Mostrar el conjunto de números primos
print(f"Números primos en el rango de {rango_inicio} a {rango_fin}:")
print(primos)
