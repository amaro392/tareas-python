def total_factura(cantidad_sin_iva, porcentaje_iva=19):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total
