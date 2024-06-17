#calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        a / b
        

# Función principal para ejecutar la calculadora
def calculadora():
    while True:
        print("\nBienvenido a la calculadora")
        print("Seleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación deseada (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print("Resultado:", sumar(num1, num2))
            elif opcion == '2':
                print("Resultado:", restar(num1, num2))
            elif opcion == '3': print("Resultado:", multiplicar(num1, num2))
            elif opcion == '4':
                print("Resultado:", dividir(num1, num2))
        else:
            print("Opción inválida. Por favor ingrese un número válido (1/2/3/4/5).")

calculadora()