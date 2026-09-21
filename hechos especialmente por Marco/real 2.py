class analizar_palabras:
    def __init__(self):
        self.palabras_unicas = set()
        self.historial_palabras = []

    def agregar_palabra(self, palabras):
        palabras = str(palabras)
        if palabras not in self.palabras_unicas:
            self.palabras_unicas.add(palabras)
            self.historial_palabras.append(palabras)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabras in args:
            self.agregar_palabra(palabras)


if __name__ == "__main__":
    analizar = analizar_palabras()
    analizar.agregar_palabra("messi")
    print(analizar.contar_palabras())
    print(analizar.agregar_multiples('messi','pedro','juan'))
    print(analizar.historial_palabras)





