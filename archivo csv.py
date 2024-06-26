import csv

# Nombre del archivo CSV donde se registrarán las ventas
FILENAME = "ventas.csv"

# Función para registrar una nueva venta
def registrar_venta():
    nombre_producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    valor_unitario = float(input("Valor unitario: "))
    forma_pago = input("Forma de pago (Efectivo, Tarjeta de débito, Tarjeta de crédito, Transferencia electrónica): ")
    precio_total = cantidad * valor_unitario

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre_producto, cantidad, valor_unitario, forma_pago, precio_total])
    
    print(f"Venta de {nombre_producto} registrada con éxito.")

# Función para mostrar el reporte de ventas histórico
def reporte_ventas_historico():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        print("Ventas históricas:")
        for row in reader:
            print(row)

# Función para generar el reporte de ventas por producto
def reporte_ventas_por_producto():
    ventas = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nombre_producto, cantidad, valor_unitario, forma_pago, precio_total = row
            cantidad = int(cantidad)
            precio_total = float(precio_total)
            if nombre_producto in ventas:
                ventas[nombre_producto]['cantidad'] += cantidad
                ventas[nombre_producto]['monto'] += precio_total
            else:
                ventas[nombre_producto] = {'cantidad': cantidad, 'monto': precio_total}
    
    with open('reporte_por_producto.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Producto", "Cantidad vendida", "Monto vendido"])
        for producto, datos in ventas.items():
            writer.writerow([producto, datos['cantidad'], datos['monto']])
    
    print("Reporte de ventas por producto generado: reporte_por_producto.csv")

# Función para generar el reporte de ventas por forma de pago
def reporte_ventas_por_forma_pago():
    ventas = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nombre_producto, cantidad, valor_unitario, forma_pago, precio_total = row
            precio_total = float(precio_total)
            if forma_pago in ventas:
                ventas[forma_pago]['cantidad'] += 1
                ventas[forma_pago]['monto'] += precio_total
            else:
                ventas[forma_pago] = {'cantidad': 1, 'monto': precio_total}
    
    with open('reporte_por_forma_pago.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Forma de pago", "Cantidad de ventas", "Monto"])
        for forma_pago, datos in ventas.items():
            writer.writerow([forma_pago, datos['cantidad'], datos['monto']])
    
    print("Reporte de ventas por forma de pago generado: reporte_por_forma_pago.csv")

# Función principal que muestra el menú y gestiona las opciones
def main():
    while True:
        print("\nMenú:")
        print("1- Registrar nueva venta")
        print("2- Reporte de ventas histórico")
        print("3- Reporte de ventas por producto")
        print("4- Reporte por formas de pago")
        print("5- Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            reporte_ventas_historico()
        elif opcion == '3':
            reporte_ventas_por_producto()
        elif opcion == '4':
            reporte_ventas_por_forma_pago()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
