class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = float(notaExamen)
        
    def __str__(self):
        return f" -Catedra: {self.catedra}, Clasificación: {self.notaExamen}"