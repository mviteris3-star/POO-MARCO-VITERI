class invertir_secuencia:
    def __init__(self):
        pass

    def invertir(self, lista):
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            invertida = self.invertir(lista)
            resultado[tuple(lista)] = invertida
        return resultado


if __name__ == '__main__':
    invertir1 = invertir_secuencia()
    print(invertir1.invertir([1, 2, 3, 4]))
    print(invertir1.invertir_multiples(1,2,4,6,7))
