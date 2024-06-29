def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = "Hola, ¿cómo estás?"
print("La cantidad de palabras en la cadena es:", contar_palabras(cadena))
