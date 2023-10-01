from Tecnologia import Tecnologia
from Transporte import Transporte
class Bicicleta(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, precio, eficiencia, aro, peso):
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia)
        Transporte.__init__(self, peso)
        self.aro = aro

    def cotizar(self):
        descuento_eficiencia = self.calcularDescuento()
        costo_despacho = self.calcularDespacho()
        total = self.precio - descuento_eficiencia + costo_despacho
        print(f"Bicicleta {self.marca}, Aro: {self.aro}, Peso: {self.peso} kg, Descuento: {descuento_eficiencia}, Despacho: {costo_despacho}, Total: {total}")