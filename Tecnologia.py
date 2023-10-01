class Tecnologia:
    def __init__(self, marca, voltaje, precio, eficiencia):
        self.marca = marca
        self.voltaje = voltaje
        self.precio = precio
        self.eficiencia = eficiencia

    def calcularDescuento(self):
        if self.eficiencia in ['A', 'B']:
            return self.precio * 0.5
        elif self.eficiencia in ['C', 'D']:
            return self.precio * 0.3
        elif self.eficiencia in ['E', 'F']:
            return self.precio * 0.1
        else:
            return 0
    
