import csv

def leer_datos_csv(nombre_archivo):
    """Lee los datos de un archivo CSV y los retorna como una lista de diccionarios."""
    datos = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            fila['ventas'] = int(fila['ventas'])
            datos.append(fila)
    return datos

def clasificar_empresas(datos):
    """Clasifica las empresas en pequeño, mediano y gran contribuyente según sus ventas."""
    pequeno_contribuyente = []
    mediano_contribuyente = []
    gran_contribuyente = []

    for empresa in datos:
        if empresa['ventas'] <= 100_000_000:
            pequeno_contribuyente.append(empresa)
        elif 100_000_001 <= empresa['ventas'] <= 200_000_000:
            mediano_contribuyente.append(empresa)
        else:
            gran_contribuyente.append(empresa)

    return pequeno_contribuyente, mediano_contribuyente, gran_contribuyente

def guardar_datos_csv(nombre_archivo, datos):
    """Guarda los datos en un archivo CSV."""
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campos = ['rut', 'nombre', 'ventas']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for fila in datos:
            escritor_csv.writerow(fila)

# Leer datos del archivo CSV
nombre_archivo_csv = 'listadoRutEmpresa.csv'
datos = leer_datos_csv(nombre_archivo_csv)

# Clasificar las empresas según sus ventas
pequeno_contribuyente, mediano_contribuyente, gran_contribuyente = clasificar_empresas(datos)

# Guardar los datos clasificados en archivos CSV
guardar_datos_csv('Pequeno_Contribuyente.csv', pequeno_contribuyente)
guardar_datos_csv('Mediano_Contribuyente.csv', mediano_contribuyente)
guardar_datos_csv('Gran_Contribuyente.csv', gran_contribuyente)

# Mostrar la clasificación de empresas
print("Pequeño Contribuyente:")
for empresa in pequeno_contribuyente:
    print(f"{empresa['rut']}, {empresa['nombre']}, {empresa['ventas']}")

print("\nMediano Contribuyente:")
for empresa in mediano_contribuyente:
    print(f"{empresa['rut']}, {empresa['nombre']}, {empresa['ventas']}")

print("\nGran Contribuyente:")
for empresa in gran_contribuyente:
    print(f"{empresa['rut']}, {empresa['nombre']}, {empresa['ventas']}")
