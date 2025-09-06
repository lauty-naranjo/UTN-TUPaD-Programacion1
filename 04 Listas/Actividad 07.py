"""
Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
    autos = ["sedan", "polo", "suran", "gol"]
"""

autos = ["sedan", "polo", "suran", "gol"]
print(autos) # lista original

autos[1:3] = ["Hayabusa", "Gsx-R1000"]
print(autos) # lista con los indices 1 y 2 reemplazados
