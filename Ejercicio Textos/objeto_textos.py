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
