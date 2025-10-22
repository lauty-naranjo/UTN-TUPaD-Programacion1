class componentesCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def calcular_subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        subtotal = self.calcular_subtotal()
        return f"{self.componente:<15} {self.marca:<15} {self.cantidad:<8} {self.precio:<15}  {subtotal}"