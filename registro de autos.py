import csv
from datetime import datetime

def agregar_accion(bitacora):
    """Función para agregar una acción a la bitácora con fecha y hora actual."""
    accion = input("Ingrese la acción realizada en el auto: ")
    fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    bitacora.append((fecha_hora_actual, accion))
    print("Acción agregada correctamente.")

def mostrar_bitacora(bitacora):
    """Función para mostrar todas las acciones registradas en la bitácora."""
    if not bitacora:
        print("La bitácora está vacía.")
    else:
        print("Bitácora de acciones del auto:")
        for fecha, accion in bitacora:
            print(f"{fecha}: {accion}")

def guardar_bitacora_csv(bitacora, nombre_archivo):
    """Función para guardar la bitácora en un archivo CSV."""
    try:
        with open(nombre_archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Fecha y Hora', 'Acción Realizada'])
            writer.writerows(bitacora)
        print(f"Bitácora guardada correctamente en '{nombre_archivo}'.")
    except IOError:
        print(f"Error: No se pudo guardar la bitácora en '{nombre_archivo}'.")

# Función principal
def main():
    bitacora = []  # Lista para almacenar las acciones con fecha y hora
    nombre_archivo = ""  # Variable para almacenar el nombre del archivo CSV

    print("Bienvenido al programa de registro histórico de acciones del auto.")

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar acción a la bitácora")
        print("2. Ver bitácora de acciones")
        print("3. Guardar bitácora en archivo CSV")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            agregar_accion(bitacora)
        
        elif opcion == '2':
            mostrar_bitacora(bitacora)
        
        elif opcion == '3':
            nombre_archivo = input("Ingrese el nombre del archivo CSV para guardar la bitácora (sin extensión): ")
            nombre_archivo += ".csv"
            guardar_bitacora_csv(bitacora, nombre_archivo)
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
