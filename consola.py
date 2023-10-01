from Tecnologia import Tecnologia
class Consola(Tecnologia):
    def __init__(self, nombreConsola, version, marca, voltaje, precio, eficiencia):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.nombreConsola = nombreConsola
        self.version = version

    def cotizar(self):
        descuento_eficiencia = self.calcularDescuento()
        descuento_total = descuento_eficiencia
        if "Lite" in self.version:
            descuento_total += self.precio * 0.05
        total = self.precio - descuento_total
        print(f"Consola {self.nombreConsola}, Versión: {self.version}, Descuento: {descuento_total}, Total: {total}")