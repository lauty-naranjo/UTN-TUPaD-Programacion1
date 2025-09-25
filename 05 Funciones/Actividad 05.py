"""
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""

# Funcion
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"{segundos} segundos son: {segundos_a_horas(segundos)} en horas.")