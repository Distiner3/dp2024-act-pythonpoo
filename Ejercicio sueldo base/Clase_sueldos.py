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
