import json

def escribir_json(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

datos = {
    "nombre": "Ana",
    "edad": 23,
    "ciudad": "Madrid",
    "amigos": ["Luis", "María", "Pedro"]
}

archivo = 'nuevos_datos.json'
escribir_json(archivo, datos)
print("Datos escritos en 'nuevos_datos.json'.")
