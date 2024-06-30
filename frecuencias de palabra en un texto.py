def contar_palabras(texto):
    # Inicializar el diccionario de frecuencias
    frecuencias = {}

    # Dividir el texto en palabras
    palabras = texto.split()

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        palabra = palabra.lower().strip(",.!?")  # Convertir a minúsculas y eliminar puntuación
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias

def mostrar_frecuencias(frecuencias):
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencias.items():
        print(f"{palabra}: {frecuencia}")

# Pedir al usuario que ingrese un texto
texto = input("Introduce un texto: ")

# Contar la frecuencia de las palabras
frecuencias = contar_palabras(texto)

# Mostrar la frecuencia de las palabras
mostrar_frecuencias(frecuencias)
