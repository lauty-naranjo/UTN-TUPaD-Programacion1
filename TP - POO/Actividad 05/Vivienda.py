from Habitacion import habitacion

class vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = int(numero)
        self.manzana = manzana
        self.nroCasa = int(nroCasa)
        self.superficieTerreno = float(superficieTerreno)
        self.lista_habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.lista_habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        metrosCubiertos = sum(habitacion.metrosCuadrados for habitacion in self.lista_habitaciones)

        if metrosCubiertos > self.superficieTerreno:
            raise Exception("La suma de los metros cuadrados cubiertos excede la superficie del terreno.")
        return metrosCubiertos
    