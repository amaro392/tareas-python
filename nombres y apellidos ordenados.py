# Ingresar 3 nombres
nombres = []
apellidos = []
for i in range(3):
    nombre = input(f"Introduce el nombre {i+1}: ")
    apellido = input(f"Introduce el apellido {i+1}: ")
    nombres.append(nombre)
    apellidos.append(apellido)

# Ordenar las listas
nombres.sort()
apellidos.sort()

# Mostrar los nombres y apellidos ordenados
print("Nombres ordenados:")
for nombre in nombres:
    print(nombre)

print("\nApellidos ordenados:")
for apellido in apellidos:
    print(apellido)
