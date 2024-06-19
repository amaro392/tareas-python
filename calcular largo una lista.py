def largo_lista_recursiva(lista):
    # Caso base: la lista está vacía
    if lista == []:
        return 0
    # Caso recursivo: reducir la lista y sumar 1 al largo calculado recursivamente
    else:
        return 1 + largo_lista_recursiva(lista[1:])

# Ejemplo de uso:
lista_ejemplo = [1, 2, 3, 4, 5]
print("Largo de la lista:", largo_lista_recursiva(lista_ejemplo))
