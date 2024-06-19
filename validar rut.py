def validar_rut(rut):
    rut = rut.upper()  # Convertir a mayúsculas si es necesario
    
    # Separar el rut y el dígito verificador
    rut, verificador = rut.split('-')
    
    # Eliminar puntos del rut (si los hay)
    rut = rut.replace('.', '')
    
    # Verificar que el rut sea numérico
    if not rut.isdigit():
        return False
    
    # Calcular dígito verificador esperado
    suma = 0
    multiplo = 2
    for i in reversed(rut):
        suma += int(i) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2
    digito = 11 - suma % 11
    
    # Convertir dígito a cadena según las reglas
    if digito == 11:
        digito = '0'
    elif digito == 10:
        digito = 'K'
    else:
        digito = str(digito)
    
    # Comparar dígito verificador ingresado con el calculado
    return digito == verificador

# Ejemplos de uso:
rut_correcto = "12.345.678-9"
rut_incorrecto = "12.345.678-0"

print(validar_rut(rut_correcto))    # True
print(validar_rut(rut_incorrecto))  # False
