"""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""

# Funcion
def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
celcius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celcius_a_fahrenheit(celcius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

