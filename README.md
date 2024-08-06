# dp2024-act-pythonpoo

Ejemplos de POO con Python

Nombre: Diego Esteban Illescas Rodríguez
Carnet: 201901851

1. Solicitar 3 textos:

import math

class Numeros:
    def __init__(self, valor):
        self.valor = valor

   def factorial(self):
        return math.factorial(self.valor)

   def es_primo(self):
        if self.valor <= 1:
            return False
        for i in range(2, int(math.sqrt(self.valor)) + 1):
            if self.valor % i == 0:
                return False
        return True

   def es_perfecto(self):
        if self.valor < 1:
            return False
        suma_divisores = sum(i for i in range(1, self.valor) if self.valor % i == 0)
        return suma_divisores == self.valor

   def a_binario(self):
        return bin(self.valor)[2:]

from Clase_numeros import Numeros

valor = int(input("Ingrese un valor numérico en base 10: "))

numero = Numeros(valor)

factorial = numero.factorial()
print(f"Factorial de {valor}: {factorial}")

es_primo = numero.es_primo()
print(f"El número {valor} {'es' if es_primo else 'no es'} primo")

es_perfecto = numero.es_perfecto()
print(f"El número {valor} {'es' if es_perfecto else 'no es'} perfecto")

binario = numero.a_binario()
print(f"El número {valor} en binario es: {binario}")

--------------------------------------------------------------------------------------------------------------------------------------------------------


2. Cálculos para un empleado del departamento de ventas:
class Empleado:
    def __init__(self, sueldo_base, ventas_realizadas, bonificacion=0):
        self.sueldo_base = sueldo_base
        self.ventas_realizadas = ventas_realizadas
        self.bonificacion = bonificacion

    def comision_por_ventas(self):
        return self.ventas_realizadas * 0.10

    def igss(self):
        return self.sueldo_base * 0.0483

    def ahorro(self):
        total_ganado = self.total_ganado()
        return total_ganado * 0.07

    def total_ganado(self):
        return self.sueldo_base + self.comision_por_ventas() + self.bonificacion

    def total_descuentos(self):
        return self.ahorro() + self.igss()

    def sueldo_liquido(self):
        return self.total_ganado() - self.total_descuentos()

from Clase_sueldos import Empleado

sueldo_base = float(input("Ingrese el sueldo base: "))
ventas_realizadas = float(input("Ingrese el valor de las ventas realizadas: "))
bonificacion = float(input("Ingrese la bonificación (si aplica, de lo contrario ingrese 0): "))

empleado = Empleado(sueldo_base, ventas_realizadas, bonificacion)

comision = empleado.comision_por_ventas()
print(f"Comisión por ventas: {comision}")

igss = empleado.igss()
print(f"IGSS: {igss}")

ahorro = empleado.ahorro()
print(f"Ahorro: {ahorro}")

total_ganado = empleado.total_ganado()
print(f"Total ganado: {total_ganado}")

total_descuentos = empleado.total_descuentos()
print(f"Total descuentos: {total_descuentos}")

sueldo_liquido = empleado.sueldo_liquido()
print(f"Sueldo líquido: {sueldo_liquido}")


--------------------------------------------------------------------------------------------------------------------------------------------------------

3. Solicitar 1 valor numérico de base 10:

class Textos:
    def __init__(self, texto1, texto2, texto3):
        self.textos = [texto1, texto2, texto3]

   def prom_longitud(self):
        total_length = sum(len(texto) for texto in self.textos)
        return total_length / len(self.textos)

   def concat_compar(self):
        concatenado = ''.join(self.textos)
        length = len(concatenado)
        if length > 15:
            return "mayor"
        elif length < 15:
            return "menor"
        else:
            return "igual"

   def texto_largo(self):
        return max(self.textos, key=len)

   def contar_numericos(self):
        concatenado = ''.join(self.textos)
        return sum(1 for char in concatenado if char.isdigit())

from clase_textos import Textos

texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")
texto3 = input("Ingrese el tercer texto: ")

textos = Textos(texto1, texto2, texto3)

promedio = textos.prom_longitud()
print(f"Promedio de las longitudes de los textos: {promedio}")

comparacion = textos.concat_compar()
print(f"La longitud del texto concatenado es {comparacion} a 15")

texto_mas_largo = textos.texto_largo()
print(f"El texto con más caracteres es: {texto_mas_largo}")

num_caracteres_numericos = textos.contar_numericos()
print(f"Cantidad de caracteres numéricos en el texto concatenado: {num_caracteres_numericos}")


--------------------------------------------------------------------------------------------------------------------------------------------------------

4. Ejemplo de Herencia

permite a una clase derivar o heredar propiedades y métodos de otra clase. La clase que hereda se llama clase derivada o subclase, y la clase de la que hereda se llama clase base o superclase. La herencia permite reutilizar código y crear relaciones jerárquicas entre clases.

class ClaseBase:
    pass

class ClaseDerivada(ClaseBase):
    pass

   Ejemplo:

    class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.sueldo = sueldo

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()  # Llama al método de la clase base
        return f"{informacion_base}, Sueldo: {self.sueldo}"


 
