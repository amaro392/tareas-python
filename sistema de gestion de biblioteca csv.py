import csv
import os
from datetime import datetime

# Archivos CSV
libros_csv = 'libros.csv'
prestamos_csv = 'prestamos.csv'

# Funciones para leer y escribir en archivos CSV
def leer_csv(archivo):
    with open(archivo, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def escribir_csv(archivo, datos, campos):
    with open(archivo, mode='w', newline='') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

def agregar_csv(archivo, datos, campos):
    file_exists = os.path.isfile(archivo)
    with open(archivo, mode='a', newline='') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        if not file_exists:
            escritor.writeheader()
        escritor.writerow(datos)

# Función para registrar un nuevo libro
def registrar_nuevo_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    anio = input("Año de publicación: ")
    isbn = input("ISBN: ")
    copias = int(input("Copias disponibles: "))

    nuevo_libro = {
        'Titulo': titulo,
        'Autor': autor,
        'Anio': anio,
        'ISBN': isbn,
        'Copias': copias
    }

    campos = ['Titulo', 'Autor', 'Anio', 'ISBN', 'Copias']
    agregar_csv(libros_csv, nuevo_libro, campos)
    print("Nuevo libro registrado.")

# Función para registrar un nuevo préstamo
def registrar_nuevo_prestamo():
    isbn = input("ISBN del libro: ")
    nombre_usuario = input("Nombre del usuario: ")
    fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    libros = leer_csv(libros_csv)
    libro_encontrado = False
    for libro in libros:
        if libro['ISBN'] == isbn and int(libro['Copias']) > 0:
            libro_encontrado = True
            libro['Copias'] = int(libro['Copias']) - 1
            break

    if libro_encontrado:
        nuevo_prestamo = {
            'ISBN': isbn,
            'Usuario': nombre_usuario,
            'Fecha': fecha_prestamo
        }
        campos_prestamos = ['ISBN', 'Usuario', 'Fecha']
        agregar_csv(prestamos_csv, nuevo_prestamo, campos_prestamos)
        escribir_csv(libros_csv, libros, ['Titulo', 'Autor', 'Anio', 'ISBN', 'Copias'])
        print("Préstamo registrado.")
    else:
        print("No hay copias disponibles o ISBN no encontrado.")

# Función para mostrar el reporte de libros disponibles
def reporte_libros_disponibles():
    libros = leer_csv(libros_csv)
    print("Libros disponibles:")
    for libro in libros:
        if int(libro['Copias']) > 0:
            print(f"Título: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Anio']}, ISBN: {libro['ISBN']}, Copias: {libro['Copias']}")

# Función para mostrar el reporte de préstamos históricos
def reporte_prestamos_historicos():
    prestamos = leer_csv(prestamos_csv)
    print("Préstamos históricos:")
    for prestamo in prestamos:
        print(f"ISBN: {prestamo['ISBN']}, Usuario: {prestamo['Usuario']}, Fecha: {prestamo['Fecha']}")

# Función para mostrar el reporte de préstamos por usuario
def reporte_prestamos_por_usuario():
    prestamos = leer_csv(prestamos_csv)
    reporte = {}
    for prestamo in prestamos:
        usuario = prestamo['Usuario']
        if usuario not in reporte:
            reporte[usuario] = 1
        else:
            reporte[usuario] += 1

    print("Reporte de préstamos por usuario:")
    for usuario, cantidad in reporte.items():
        print(f"Usuario: {usuario}, Préstamos: {cantidad}")

# Función principal del menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar nuevo libro")
        print("2. Registrar nuevo préstamo")
        print("3. Reporte de libros disponibles")
        print("4. Reporte de préstamos históricos")
        print("5. Reporte de préstamos por usuario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_nuevo_libro()
        elif opcion == '2':
            registrar_nuevo_prestamo()
        elif opcion == '3':
            reporte_libros_disponibles()
        elif opcion == '4':
            reporte_prestamos_historicos()
        elif opcion == '5':
            reporte_prestamos_por_usuario()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
menu()
