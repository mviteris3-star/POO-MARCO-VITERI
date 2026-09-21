class articulos:
    def __init__(self):
        self.articulos = {}

    def agregar_articulos(self, nombre, precio):
        self.articulos[nombre] = float(precio)

    def total_articulos(self):
        return sum(self.articulos.values())

    def articulos_rango(self, rango_min, rango_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if rango_min <= precio <= rango_max:
                resultado.append(nombre)
        return resultado

if __name__ == "__main__":
    articulos = articulos()
    print(articulos.total_articulos())
    articulos.agregar_articulos('pan', 2)
    articulos.agregar_articulos('cola', 3)
    print(articulos.articulos_rango(1, 5))