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
