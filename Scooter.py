from Tecnologia import Tecnologia
from Transporte import Transporte
class Scooter(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, precio, eficiencia, aro, velocidad, peso):
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia)
        Transporte.__init__(self, peso)
        self.aro = aro
        self.velocidad = velocidad

    def cotizar(self):
        descuento_eficiencia = self.calcularDescuento()
        costo_despacho = self.calcularDespacho()
        total = self.precio - descuento_eficiencia + costo_despacho
        print(f"Scooter {self.marca}, Aro: {self.aro}, Velocidad: {self.velocidad} km/h, Peso: {self.peso} kg, Descuento: {descuento_eficiencia}, Despacho: {costo_despacho}, Total: {total}")