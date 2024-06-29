def convertir_mayusculas(cadena):
    mayusculas = ""
    for caracter in cadena:
        if 'a' <= caracter <= 'z':
            mayusculas += chr(ord(caracter) - 32)
        else:
            mayusculas += caracter
    return mayusculas

cadena = "hola mundo"
print("La cadena en mayúsculas es:", convertir_mayusculas(cadena))
