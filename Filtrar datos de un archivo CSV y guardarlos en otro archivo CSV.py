import csv

def filtrar_csv(archivo_entrada, archivo_salida, columna, valor):
    with open(archivo_entrada, newline='') as csvfile_entrada:
        lector = csv.DictReader(csvfile_entrada)
        with open(archivo_salida, mode='w', newline='') as csvfile_salida:
            escritor = csv.DictWriter(csvfile_salida, fieldnames=lector.fieldnames)
            escritor.writeheader()
            for fila in lector:
                if fila[columna] == valor:
                    escritor.writerow(fila)

archivo_entrada = 'datos.csv'  # Asegúrate de que el archivo 'datos.csv' exista en el mismo directorio
archivo_salida = 'datos_filtrados.csv'
columna = 'Ciudad'
valor = 'Madrid'
filtrar_csv(archivo_entrada, archivo_salida, columna, valor)
print(f"Datos filtrados guardados en '{archivo_salida}'.")
