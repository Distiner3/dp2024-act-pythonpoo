# dp2024-act-pythonpoo

Ejemplos de POO con Python

Nombre: Diego Esteban Illescas Rodríguez
Carnet: 201901851

1. Solicitar 3 textos y realizar lo siguiente:
• Mostrar el promedio de las longitudes de los textos.
• Concatenar los textos e indicar si el largo es mayor, menor o igual a 15.
• Indicar cuál de los textos posee más caracteres.
• Concatenar los textos e indicar la cantidad de caracteres numéricos existentes.
--------------------------------------------------------------------------------------------------------------------------------------------------------
2. Realizar los siguientes cálculos para un empleado del departamento de ventas:
• Comisión por ventas (10% del total vendido)
• Monto para pagar de IGSS (4.83% del sueldo base)
• Ahorro (7% del total ganado)
• Total ganado = sueldo base + comisión por ventas + bonificación.
• Total descuentos = ahorro + IGSS.
• Sueldo liquido = Total ganado – total descuentos.

--------------------------------------------------------------------------------------------------------------------------------------------------------

3. Solicitar 1 valor numérico de base 10 y realizar lo siguiente: • Calcular y mostrar factorial del valor
ingresado
• Indicar si el número es primo.
• Indicar si el número es perfecto.
• Convertir el número a binario
• Mostrar la serie de Fibonacci hasta el valor ingresado.

--------------------------------------------------------------------------------------------------------------------------------------------------------

4. Ejemplo de Herencia

Permite a una clase derivar o heredar propiedades y métodos de otra clase. La clase que hereda se llama clase derivada o subclase, y la clase de la que hereda se llama clase base o superclase. La herencia permite reutilizar código y crear relaciones jerárquicas entre clases.

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


 
