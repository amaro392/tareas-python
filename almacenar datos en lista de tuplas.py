def ingresar_datos():
    """Solicita al usuario ingresar nombres y edades, y almacena los datos en una lista de tuplas."""
    datos = []
    while True:
        nombre = input("Introduce el nombre: ")
        edad = int(input("Introduce la edad: "))
        datos.append((nombre, edad))
        
        continuar = input("¿Deseas agregar otro nombre y edad? (sí/no): ").lower()
        if continuar == "no":
            break
    return datos

def obtener_edades_unicas(datos):
    """Obtiene las edades únicas de la lista de tuplas."""
    edades = {edad for _, edad in datos}
    return edades

# Ingresar datos
datos = ingresar_datos()

# Obtener las edades únicas
edades_unicas = obtener_edades_unicas(datos)

# Mostrar los resultados
print("Datos ingresados:")
for nombre, edad in datos:
    print(f"Nombre: {nombre}, Edad: {edad}")

print("\nEdades únicas:")
print(edades_unicas)
