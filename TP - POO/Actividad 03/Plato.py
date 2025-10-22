from Ingrediente import ingrediente

class plato:
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = float(precio)
        self.esBebida = esBebida
        self.listaIngredientes = []
    
    def agregarIngrediente(self, ingrediente):
        self.listaIngredientes.append(ingrediente)
    
    def __str__(self):
        return f"{self.nombreCompleto}"
    
    def mostrarInfo(self):
        info = f"{self.nombreCompleto}\n"
        info += f"Precio: ${self.precio}\n"

        if not self.esBebida:
            info += "Ingredientes:\n"
            info += f"{"Nombre":<15} {"Cantidad":<8} {"Unidad de Medida"}\n"
            for ingrediente in self.listaIngredientes:
                info += f"-{ingrediente}\n"
        
        return info