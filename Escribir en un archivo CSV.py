import csv

def escribir_csv(archivo, datos):
    with open(archivo, mode='w', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerows(datos)

datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', '23', 'Madrid'],
    ['Luis', '34', 'Barcelona'],
    ['María', '29', 'Valencia']
]

archivo = 'nuevos_datos.csv'
escribir_csv(archivo, datos)
print("Datos escritos en 'nuevos_datos.csv'.")
