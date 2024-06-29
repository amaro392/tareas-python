import csv

def escribir_diccionarios_csv(archivo, datos):
    if len(datos) == 0:
        return
    
    with open(archivo, mode='w', newline='') as csvfile:
        fieldnames = datos[0].keys()
        escritor = csv.DictWriter(csvfile, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos)

datos = [
    {'Nombre': 'Ana', 'Edad': '23', 'Ciudad': 'Madrid'},
    {'Nombre': 'Luis', 'Edad': '34', 'Ciudad': 'Barcelona'},
    {'Nombre': 'María', 'Edad': '29', 'Ciudad': 'Valencia'}
]

archivo = 'diccionarios_datos.csv'
escribir_diccionarios_csv(archivo, datos)
print("Datos escritos en 'diccionarios_datos.csv'.")
