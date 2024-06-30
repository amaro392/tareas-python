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

def es_ganador(run):
    """Verifica si el run termina en 92, 95 o 84 antes del dígito verificador."""
    ultimos_dos_digitos = run[:-2][-2:]
    return ultimos_dos_digitos in ['92', '95', '84']

def procesar_datos(datos):
    """Procesa los datos para identificar los ganadores del sorteo."""
    ganadores = []
    for persona in datos:
        run = persona['run']
        if es_ganador(run):
            ganadores.append(persona)
    return ganadores

def guardar_datos_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(nombre_archivo, mode='w', encoding='utf-8') as archivo_json:
        json.dump(datos, archivo_json, ensure_ascii=False, indent=4)

# Leer datos del archivo CSV
nombre_archivo_csv = 'listadoRun.csv'
datos = leer_datos_csv(nombre_archivo_csv)

# Procesar los datos para obtener la lista de ganadores
ganadores = procesar_datos(datos)

# Guardar la lista de ganadores en un archivo JSON
nombre_archivo_json = 'ganadores.json'
guardar_datos_json(nombre_archivo_json, ganadores)

# Mostrar los ganadores
print("Ganadores del sorteo 'La suerte de un RUN':")
for ganador in ganadores:
    print(f"RUN: {ganador['run']}, Nombre: {ganador['nombre']}")
