def validar_lista_numeros():
    """Función para validar que todos los elementos de la lista sean números enteros."""
    while True:
        numeros_str = input("Ingrese una lista de números enteros separados por espacios: ")
        numeros = numeros_str.split()

        try:
            numeros = [int(num) for num in numeros]
            return numeros
        except ValueError:
            print("Error: Ingrese únicamente números enteros. Intente nuevamente.")

def identificar_pares_impares(lista_numeros):
    """Función para identificar números pares e impares en una lista de números."""
    numeros_pares = []
    numeros_impares = []

    for num in lista_numeros:
        if num % 2 == 0:
            numeros_pares.append(num)
        else:
            numeros_impares.append(num)

    return numeros_pares, numeros_impares

# Función principal
def main():
    print("Programa para identificar números pares e impares en una lista de números enteros.")
    print("Por favor, siga las instrucciones:")

    # Validar la lista de números ingresada por el usuario
    lista_numeros = validar_lista_numeros()

    # Identificar números pares e impares
    pares, impares = identificar_pares_impares(lista_numeros)

    # Mostrar los resultados
    print("\nNúmeros pares:")
    if pares:
        print(", ".join(map(str, pares)))
    else:
        print("No se encontraron números pares.")

    print("\nNúmeros impares:")
    if impares:
        print(", ".join(map(str, impares)))
    else:
        print("No se encontraron números impares.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
