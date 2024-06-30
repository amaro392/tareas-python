# Inicializar la lista de nombres
nombres = []

# Ingresar nombres hasta que la respuesta sea "no"
while True:
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
    continuar = input("¿Deseas agregar otro nombre? (sí/no): ").lower()
    if continuar == "no":
        break

# Determinar y eliminar el nombre con la menor cantidad de caracteres
nombre_menor = min(nombres, key=len)
nombres.remove(nombre_menor)

# Mostrar los nombres restantes
print("Lista de nombres después de eliminar el nombre con menos caracteres:")
for nombre in nombres:
    print(nombre)
