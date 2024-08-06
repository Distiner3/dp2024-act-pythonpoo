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
