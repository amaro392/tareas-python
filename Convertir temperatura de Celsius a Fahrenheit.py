def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
print("La temperatura en Fahrenheit es:", celsius_a_fahrenheit(celsius))
