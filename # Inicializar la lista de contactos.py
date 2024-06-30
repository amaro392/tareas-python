# Inicializar la lista de contactos
contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
    else:
        print(f"El contacto {nombre} no existe.")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print(f"El contacto {nombre} no existe.")

# Ejemplo de uso
agregar_contacto("Juan", "123-456-789")
agregar_contacto("Ana", "987-654-321")
eliminar_contacto("Pedro")
buscar_contacto("Juan")
buscar_contacto("Pedro")
