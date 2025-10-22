from ComponentesCPU import componentesCPU

class computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.objetos_componentes = []
        self.costo_total = 0

    def agregar_componente(self, componente):
        self.objetos_componentes.append(componente)

    def calcular_costo_total(self):
        costo = sum(componente.calcular_subtotal() for componente in self.objetos_componentes)
        self.costo_total = costo

        return self.costo_total
    
    def calcular_precio_venta(self):
        costo = self.calcular_costo_total()
        margen_porcentaje = 0.0

        if costo < 50000:
            margen_porcentaje = 0.40
        else:
            margen_porcentaje = 0.30

        margen = costo * margen_porcentaje
        precio_venta = costo + margen

        return costo, margen, precio_venta
    
    def generar_informe(self):

        costo, margen, precio_venta = self.calcular_precio_venta()

        info = "\n----------- Informe de la Computadora -----------\n"
        info += f"Marca: {self.marca}\n"
        info += f"Modelo: {self.modelo}\n"
        info += "Componentes:\n"

        info += f"{'Componente':<15} {'Marca':<15} {'Cantidad':<8} {'Precio X Unidad':<15}  {'SubTotal'}\n"
        info += f"{'----------':<15} {'-----':<15} {'--------':<8} {'---------------':<15}  {'--------'}\n"

        for componente in self.objetos_componentes:
            info += f"{componente}\n"

        info += f"\nCosto Total: ${costo}\n"
        info += f"El precio sugerido de venta es: ${precio_venta}\n"
        info += "-----------------------------------------------\n"

        return info