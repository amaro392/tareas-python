# Ingresar 3 nombres
nombres = []
for i in range(3):
    nombre = input(f"Introduce el nombre {i+1}: ")
    nombres.append(nombre)

# Determinar el nombre con mayor cantidad de caracteres
nombre_mayor = max(nombres, key=len)

# Mostrar el resultado
print(f"El nombre con la mayor cantidad de caracteres es: {nombre_mayor}")
