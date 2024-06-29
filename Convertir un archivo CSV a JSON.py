import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    datos = []
    with open(archivo_csv, newline='') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            datos.append(fila)
    
    with open(archivo_json, 'w') as jsonfile:
        json.dump(datos, jsonfile, indent=4)

archivo_csv = 'datos.csv'  # Asegúrate de que el archivo 'datos.csv' exista en el mismo directorio
archivo_json = 'datos_convertidos.json'
csv_a_json(archivo_csv, archivo_json)
print(f"Archivo CSV '{archivo_csv}' convertido a JSON '{archivo_json}'.")
