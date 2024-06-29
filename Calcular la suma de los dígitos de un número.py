def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero = int(input("Ingrese un número: "))
print("La suma de los dígitos es:", suma_digitos(numero))
