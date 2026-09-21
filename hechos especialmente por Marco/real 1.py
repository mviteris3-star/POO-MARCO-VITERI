class calificador:
    def __init__(self):
        self.nota = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota:
                self.nota.append(nota)
            return self.nota

    def promedio(self):
        if not self.nota:
            return 0.0
        return sum(self.nota)/len(self.nota)

if __name__ == "__main__":


    calificador = calificador()
    print(calificador.validar_nota(20))
    print(calificador.cargar_notas(56,32,-90,103))
    print(calificador.promedio())