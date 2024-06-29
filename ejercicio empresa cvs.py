import csv

# Archivos de entrada y salida
entrada_csv = 'listadoRutEmpresa.csv'
pequeno_contribuyente_csv = 'Pequeno_Contribuyente.csv'
mediano_contribuyente_csv = 'Mediano_Contribuyente.csv'
gran_contribuyente_csv = 'Gran_Contribuyente.csv'

# Función para leer el archivo de entrada
def leer_archivo(archivo):
    with open(archivo, newline='') as csvfile:
        lector = csv.DictReader(csvfile)
        return list(lector)

# Función para escribir en un archivo CSV
def escribir_archivo(archivo, datos, campos):
    with open(archivo, mode='w', newline='') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

# Leer el archivo de entrada
empresas = leer_archivo(entrada_csv)

# Inicializar listas para clasificar las empresas
pequeno_contribuyentes = []
mediano_contribuyentes = []
gran_contribuyentes = []

# Clasificar las empresas según las ventas
for empresa in empresas:
    ventas = int(empresa['ventas'])
    if ventas <= 100000000:
        pequeno_contribuyentes.append(empresa)
    elif 100000001 <= ventas <= 200000000:
        mediano_contribuyentes.append(empresa)
    else:
        gran_contribuyentes.append(empresa)

# Definir los campos de los archivos de salida
campos = ['rut', 'nombre', 'ventas']

# Escribir los datos clasificados en los archivos correspondientes
escribir_archivo(pequeno_contribuyente_csv, pequeno_contribuyentes, campos)
escribir_archivo(mediano_contribuyente_csv, mediano_contribuyentes, campos)
escribir_archivo(gran_contribuyente_csv, gran_contribuyentes, campos)

print("Archivos generados con éxito.")
