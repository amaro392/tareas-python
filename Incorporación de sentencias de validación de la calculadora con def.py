def validar_numero(entrada):
    """Función para validar que la entrada sea un número y convertirla a float si es entero."""
    try:
        valor = float(entrada)
        return valor
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None

def sumar(a, b):
    """Función para sumar dos números."""
    return a + b

def restar(a, b):
    """Función para restar dos números."""
    return a - b

def dividir(a, b):
    """Función para dividir dos números."""
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    else:
        return a / b

def multiplicar(a, b):
    """Función para multiplicar dos números."""
    return a * b

# Función principal para interactuar con el usuario
def calculadora():
    print("Bienvenido a la calculadora")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    opcion = input("Seleccione la operación (1/2/3/4): ")

    if opcion not in ['1', '2', '3', '4']:
        print("Opción no válida")
        return

    num1 = input("Ingrese el primer número: ")
    num1 = validar_numero(num1)
    if num1 is None:
        return

    num2 = input("Ingrese el segundo número: ")
    num2 = validar_numero(num2)
    if num2 is None:
        return

    if opcion == '3' and num2 == 0:
        print("Error: No se puede dividir por cero.")
        return

    if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"El resultado de sumar {num1} y {num2} es: {resultado}")
    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"El resultado de restar {num2} de {num1} es: {resultado}")
    elif opcion == '3':
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f"El resultado de dividir {num1} entre {num2} es: {resultado}")
    elif opcion == '4':
        resultado = multiplicar(num1, num2)
        print(f"El resultado de multiplicar {num1} por {num2} es: {resultado}")

# Ejecutar la calculadora
calculadora()
