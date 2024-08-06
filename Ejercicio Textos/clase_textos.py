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
