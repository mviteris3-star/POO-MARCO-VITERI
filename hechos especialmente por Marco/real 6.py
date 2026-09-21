class gestor_tem:
    def __init__(self):
        self.temperatura = []

    def registrar_tem(self, temperatura):
        self.temperatura.append(float(temperatura))

    def registrar_multi(self, *temperaturas):
        for temperatura in temperaturas:
            self.registrar_tem(temperatura)
        return self.temperatura

    def minima(self):
        if not self.temperatura:
            return None
        return min(self.temperatura)
    def maxima(self):
        if not self.temperatura:
            return None
        return max(self.temperatura)
    def prom(self):
        if not self.temperatura:
            return None
        return sum(self.temperatura)/len(self.temperatura)

if __name__ == "__main__":
    gestor_tem = gestor_tem()
    print(gestor_tem.registrar_multi(20, 25, 18, 30))
    print(gestor_tem.prom())
    print(gestor_tem.minima())
    print(gestor_tem.maxima())



