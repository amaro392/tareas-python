import json
import csv

def json_a_csv(archivo_json, archivo_csv):
    with open(archivo_json, 'r') as jsonfile:
        datos = json.load(jsonfile)
    
    with open(archivo_csv, 'w', newline='') as csvfile:
        if len(datos) > 0:
            encabezados = datos[0].keys()
            escritor = csv.DictWriter(csvfile, fieldnames=encabezados)
            escritor.writeheader()
            for fila in datos:
                escritor.writerow(fila)

archivo_json = 'datos.json'  # Asegúrate de que el archivo 'datos.json' exista en el mismo directorio
archivo_csv = 'datos_convertidos.csv'
json_a_csv(archivo_json, archivo_csv)
print(f"Archivo JSON '{archivo_json}' convertido a CSV '{archivo_csv}'.")
