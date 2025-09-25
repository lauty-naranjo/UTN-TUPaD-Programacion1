"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado 
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
# Función
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if (b == 0):
        division = "No se puede dividir por cero"
    else:
        division = a / b
    
    return (suma, resta, multiplicacion, division)

# Programa principal
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
