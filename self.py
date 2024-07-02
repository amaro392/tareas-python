class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def obtener_edad(self):
        return self.edad

# Crear una instancia de la clase Perro
mi_perro = Perro("Fido", 3)

# Llamar a los métodos de la instancia
mi_perro.ladrar()  # Salida: Fido dice: ¡Guau!
print(mi_perro.obtener_edad())  # Salida: 3



#Acceder a los atributos y métodos de la instancia:
#self permite a los métodos acceder a los atributos y otros métodos de la instancia de la clase. Por ejemplo, puedes usar self para almacenar datos específicos de la instancia o para llamar a otros métodos de la misma instancia.

#Distinguir entre variables locales y atributos de instancia:
#Usar self ayuda a diferenciar entre variables locales (que son propias del método) y atributos de instancia (que pertenecen a la instancia de la clase).