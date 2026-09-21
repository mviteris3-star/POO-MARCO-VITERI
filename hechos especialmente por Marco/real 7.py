class ges_personas:
    def __init__(self):
        self.personas = {}

    def agregar_per(self , nombre, edad):
        self.personas[nombre]= edad

    def personas_mayores(self, edad_maxi):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad < edad_maxi:
                resultado.append(nombre)
        return resultado

    def promedio(self):
        if not self.personas:
            return 0.0
        return sum(self.personas.values()) / len(self.personas)

if __name__ == '__main__':
    personas = ges_personas()
    print(personas.promedio())
    print(personas.personas_mayores(10))
    print(personas.personas)
    personas.agregar_per('julaim', 15)
