from Nota import Nota

class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.lista_notas = []

    def agregar_nota(self, nota):
        self.lista_notas.append(nota)
    
    def calcular_promedio(self):
        total_notas = len(self.lista_notas)

        if total_notas == 0:
            return 0.0
        
        suma_notas = sum(nota.notaExamen for nota in self.lista_notas)
        return suma_notas / total_notas
    
    def __str__(self):
        return f" --- Alumno: {self.nombreCompleto}, legajo: {self.legajo} --- "