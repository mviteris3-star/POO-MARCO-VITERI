class analizador_numeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for num in numeros:
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)

        return{
            'pares': self.pares,
            'impares': self.impares
            }

    def cantidad_pares_impares(self):
        cantidad_par = len(self.pares)
        cantidad_impa = len(self.impares)
        return cantidad_par, cantidad_impa

if __name__ == '__main__':
    analizador = analizador_numeros()
    print(analizador.cantidad_pares_impares())
    print(analizador.cantidad_pares_impares())
    print(analizador.separar)
    print(analizador.pares)
    print(analizador.impares)
