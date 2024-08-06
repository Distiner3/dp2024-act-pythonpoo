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
