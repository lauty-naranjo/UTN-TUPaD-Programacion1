"""
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área 
del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el 
perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

# Funciones
def calcular_area_circulo(radio):
    area = 3.14 * radio * radio
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro


# Programa principal
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")