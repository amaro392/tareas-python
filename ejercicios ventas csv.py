import csv
from collections import defaultdict

# Función para registrar una nueva venta
def registrar_venta():
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    valor_unitario = float(input("Ingrese el valor unitario del producto: "))
    forma_pago = input("Ingrese la forma de pago (Efectivo/Debito/Credito/Transferencia): ").capitalize()

    # Calcular el precio total
    precio_total = cantidad * valor_unitario

    # Guardar la venta en el archivo CSV
    with open('ventas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre_producto, cantidad, valor_unitario, forma_pago, precio_total])

    print("Venta registrada exitosamente.")

# Función para generar reporte de ventas histórico
def reporte_ventas_historico():
    try:
        with open('ventas.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            print("\nReporte de Ventas Histórico:")
            print("{:<20} {:<10} {:<15} {:<20} {:<10}".format('Nombre Producto', 'Cantidad', 'Valor Unitario', 'Forma de Pago', 'Precio Total'))
            print("-" * 75)
            for row in reader:
                print("{:<20} {:<10} {:<15} {:<20} ${:<10}".format(row[0], row[1], row[2], row[3], row[4]))
    except FileNotFoundError:
        print("No se encontraron ventas registradas.")

# Función para generar reporte de ventas por producto
def reporte_ventas_producto():
    productos = defaultdict(lambda: {'cantidad': 0, 'monto': 0})

    try:
        with open('ventas.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Salta la cabecera
            for row in reader:
                productos[row[0]]['cantidad'] += int(row[1])
                productos[row[0]]['monto'] += float(row[4])

        with open('ventas_por_producto.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Producto', 'Cantidad vendida', 'Monto vendido'])
            for producto, data in productos.items():
                writer.writerow([producto, data['cantidad'], f"${data['monto']}"])

        print("\nReporte de Ventas por Producto generado correctamente.")
    except FileNotFoundError:
        print("No se encontraron ventas registradas.")

# Función para generar reporte de ventas por forma de pago
def reporte_ventas_forma_pago():
    formas_pago = defaultdict(lambda: {'cantidad': 0, 'monto': 0})

    try:
        with open('ventas.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Salta la cabecera
            for row in reader:
                formas_pago[row[3]]['cantidad'] += 1
                formas_pago[row[3]]['monto'] += float(row[4])

        with open('ventas_por_forma_pago.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Forma de Pago', 'Cantidad de Ventas', 'Monto'])
            for forma_pago, data in formas_pago.items():
                writer.writerow([forma_pago, data['cantidad'], f"${data['monto']}"])

        print("\nReporte de Ventas por Forma de Pago generado correctamente.")
    except FileNotFoundError:
        print("No se encontraron ventas registradas.")

# Función principal del programa
def main():
    while True:
        print("\nMenú Principal:")
        print("1. Registrar nueva venta")
        print("2. Reporte de ventas histórico")
        print("3. Reporte de ventas por producto")
        print("4. Reporte por formas de pago")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            registrar_venta()
        
        elif opcion == '2':
            reporte_ventas_historico()
        
        elif opcion == '3':
            reporte_ventas_producto()
        
        elif opcion == '4':
            reporte_ventas_forma_pago()
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el programa
if __name__ == "__main__":
    main()
