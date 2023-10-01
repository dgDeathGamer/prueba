from Tecnologia import Tecnologia
class Tv(Tecnologia):
    def __init__(self, marca, voltaje, precio, eficiencia, tamaño):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.tamaño = tamaño

    def cotizar(self):
        descuento_eficiencia = self.calcularDescuento()
        total = self.precio - descuento_eficiencia
        print(f"TV {self.marca}, Tamaño: {self.tamaño} pulgadas, Descuento: {descuento_eficiencia}, Total: {total}")