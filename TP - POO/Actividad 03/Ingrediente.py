class ingrediente:
    def __init__(self, nombre, cantidad, unidad_de_medida):
        self.nombre = nombre
        self.cantidad = float(cantidad)
        self.unidad_de_medida = unidad_de_medida

    def __str__(self):
        return f"{self.nombre:<15} {self.cantidad:<8} {self.unidad_de_medida}"