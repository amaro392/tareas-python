def crear_matriz(filas, columnas):
    """Función para crear una matriz con valores ingresados por el usuario."""
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese el elemento para la posición [{i+1},{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    """Función para mostrar una matriz en formato legible."""
    for fila in matriz:
        print(fila)

def sumar_matrices(matriz1, matriz2):
    """Función para sumar dos matrices."""
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Error: Las matrices deben ser del mismo tamaño para sumarlas.")
        return None

    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    """Función para multiplicar dos matrices."""
    if len(matriz1[0]) != len(matriz2):
        print("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para multiplicarlas.")
        return None

    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            producto = 0
            for k in range(len(matriz2)):
                producto += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(producto)
        resultado.append(fila_resultado)
    
    return resultado

# Función principal
def main():
    print("Bienvenido al programa de operaciones con matrices escalares.")
    
    while True:
        print("\nMenú de opciones:")
        print("1. Sumar matrices")
        print("2. Multiplicar matrices")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            try:
                filas = int(input("Ingrese el número de filas de las matrices: "))
                columnas = int(input("Ingrese el número de columnas de las matrices: "))
                print("\nIngrese la primera matriz:")
                matriz1 = crear_matriz(filas, columnas)
                print("\nIngrese la segunda matriz:")
                matriz2 = crear_matriz(filas, columnas)
                resultado = sumar_matrices(matriz1, matriz2)
                if resultado:
                    print("\nResultado de la suma de matrices:")
                    mostrar_matriz(resultado)
            except ValueError:
                print("Error: Ingrese un número entero válido para filas y columnas.")
        
        elif opcion == '2':
            try:
                filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
                columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))
                filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
                columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
                if columnas1 != filas2:
                    print("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
                    continue
                print("\nIngrese la primera matriz:")
                matriz1 = crear_matriz(filas1, columnas1)
                print("\nIngrese la segunda matriz:")
                matriz2 = crear_matriz(filas2, columnas2)
                resultado = multiplicar_matrices(matriz1, matriz2)
                if resultado:
                    print("\nResultado de la multiplicación de matrices:")
                    mostrar_matriz(resultado)
            except ValueError:
                print("Error: Ingrese un número entero válido para filas y columnas.")
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
