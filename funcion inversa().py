def inversa():
    cadena_original = input("Ingresa una cadena: ")
    longitud = len(cadena_original)
    cadena_invertida = ''
    for i in range(longitud - 1, -1, -1):
        cadena_invertida += cadena_original[i]
    return cadena_invertida

# Ejemplo de uso:
cadena_invertida = inversa()
print("Cadena invertida:", cadena_invertida)
