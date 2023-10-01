class Transporte:
    COSTODESPACHOBASE = 4000

    def __init__(self, peso):
        self.peso = peso

    def calcularDespacho(self):
        costo_despacho = Transporte.COSTODESPACHOBASE + self.peso * 300
        return costo_despacho