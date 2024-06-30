import csv
import json

def leer_datos_csv(nombre_archivo):
    """Lee los datos de un archivo CSV y los retorna como una lista de diccionarios."""
    datos = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def procesar_datos(datos):
    """Procesa los datos para determinar si cada persona es mayor o menor de edad."""
    mayores = []
    for persona in datos:
        nombre = persona['nombre']
        edad = int(persona['edad'])
        comuna = persona['comuna']
        estado_edad = 'Mayor de edad' if edad >= 18 else 'Menor de edad'
        print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
        if edad >= 25:
            mayores.append(persona)
    return mayores

def guardar_datos_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(nombre_archivo, mode='w', encoding='utf-8') as archivo_json:
        json.dump(datos, archivo_json, ensure_ascii=False, indent=4)

# Leer datos del archivo CSV
nombre_archivo_csv = 'datos.csv'
datos = leer_datos_csv(nombre_archivo_csv)

# Procesar los datos y obtener la lista de personas mayores o iguales a 25 años
mayores = procesar_datos(datos)

# Guardar la lista de personas mayores o iguales a 25 años en un archivo JSON
nombre_archivo_json = 'mayores.json'
guardar_datos_json(nombre_archivo_json, mayores)
