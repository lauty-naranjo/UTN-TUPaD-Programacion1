from Vivienda import vivienda

class barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.listaViviendas = []

    def agregar_vivienda(self, vivienda):
        self.listaViviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        superficieTotal = sum(vivienda.superficieTerreno for vivienda in self.listaViviendas)
        return superficieTotal
    
    def getSuperficieTotalTerrenoXManzana(self, manzana):
        superficileTotalManzana = 0

        for vivienda in self.listaViviendas:
            if vivienda.manzana.lower() == manzana.lower():
                superficileTotalManzana += vivienda.superficieTerreno
            else:
                return "No existen viviendas en esa manzana."

        return superficileTotalManzana
    
    def getSuperficieTotalCubierta(self):
        superficieTotalCubierta = sum(vivienda.getMetrosCuadradosCubiertos() for vivienda in self.listaViviendas)
        return superficieTotalCubierta