def calcular_promedio():
    numeros = []
    while True:
        entrada = input("Ingresa un número (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.")

    if not numeros:
        print("No se ingresaron números.")
        return

    suma_total = sum(numeros)
    promedio = suma_total / len(numeros)
    return promedio

# Ejemplo de uso:
promedio = calcular_promedio()
if promedio is not None:
    print(f"El promedio de los números ingresados es: {promedio}")
