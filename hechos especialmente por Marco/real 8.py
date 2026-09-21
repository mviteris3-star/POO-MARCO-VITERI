class Equipos:
    def __init__(self):
        self.equipos = []

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos.append(nombre_equipo)
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.crear_equipo[equipo].append(jugador)

    def equipo_mayor(self):
        if not self.equipos:
            return None
        return max(self.equipos, key=lambda eq: len(self.equipos[eq]))

if __name__ == '__main__':
    personas = Equipos()
    personas.agregar_jugador('julaim', 10)
    personas.agregar_jugador('julaim', 20)
    print(personas.equipo_mayor())
    print(personas.equipo_mayor())


