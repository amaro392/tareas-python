import csv
from datetime import datetime

# Definir las comunas
comunas = ["Centro", "Norte", "Sur"]

# Función para registrar un pedido
def registrar_pedido():
    nombre = input("Ingrese el nombre y apellido del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    comuna = input("Ingrese la comuna (Centro, Norte, Sur): ")

    if comuna not in comunas:
        print("Comuna no válida. Intente nuevamente.")
        return

    libro = input("Ingrese el título del libro: ")
    try:
        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        precio_unitario = float(input("Ingrese el precio unitario del libro: "))
    except ValueError:
        print("Cantidad o precio no válido. Intente nuevamente.")
        return

    valor = cantidad * precio_unitario
    descuento = 0
    if comuna == "Centro":
        descuento = valor * 0.10

    valor_final = valor - descuento

    pedido = {
        "Cliente": nombre,
        "Dirección": direccion,
        "Comuna": comuna,
        "Libro": libro,
        "Cantidad": cantidad,
        "Precio Unitario": precio_unitario,
        "Valor": valor,
        "Descuento %": 10 if comuna == "Centro" else 0,
        "Descuento $": descuento,
        "Valor final": valor_final
    }

    with open('pedidos_libreria.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=pedido.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(pedido)

    print("Pedido registrado con éxito.")

# Función para listar todos los pedidos
def listar_pedidos():
    try:
        with open('pedidos_libreria.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No hay pedidos registrados.")

# Función para imprimir la hoja de ruta
def imprimir_hoja_ruta():
    comuna_seleccionada = input("Ingrese la comuna para imprimir la hoja de ruta (Centro, Norte, Sur): ")

    if comuna_seleccionada not in comunas:
        print("Comuna no válida. Intente nuevamente.")
        return

    pedidos_comuna = []

    try:
        with open('pedidos_libreria.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Comuna"] == comuna_seleccionada:
                    pedidos_comuna.append(row)
    except FileNotFoundError:
        print("No hay pedidos registrados.")
        return

    if not pedidos_comuna:
        print(f"No hay pedidos para la comuna {comuna_seleccionada}.")
        return

    filename = f"hoja_ruta_{comuna_seleccionada.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=pedidos_comuna[0].keys())
        writer.writeheader()
        writer.writerows(pedidos_comuna)

    print(f"Hoja de ruta para {comuna_seleccionada} guardada en {filename}.")

# Función principal
def main():
    while True:
        print("\nSistema de Gestión de Pedidos - Libros y Más")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            listar_pedidos()
        elif opcion == '3':
            imprimir_hoja_ruta()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
