import math

def mostrar_menu_principal():
    print("Bienvenido al programa de cálculo de áreas y perímetros")
    print("1. Calcular área y perímetro de un círculo")
    print("2. Calcular área y perímetro de un cuadrado")
    print("3. Calcular área y perímetro de un rectángulo")
    print("4. Salir")

def calcular_area_perimetro_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

def calcular_area_perimetro_cuadrado():
    lado = float(input("Ingresa la longitud del lado del cuadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"El área del cuadrado es: {area:.2f}")
    print(f"El perímetro del cuadrado es: {perimetro:.2f}")

def calcular_area_perimetro_rectangulo():
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"El área del rectángulo es: {area:.2f}")
    print(f"El perímetro del rectángulo es: {perimetro:.2f}")

# Función principal del programa
def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            calcular_area_perimetro_circulo()
        elif opcion == '2':
            calcular_area_perimetro_cuadrado()
        elif opcion == '3':
            calcular_area_perimetro_rectangulo()
        elif opcion == '4':
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida (1-4).")

if __name__ == "__main__":
    main()
