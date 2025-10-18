"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
    -La solución debe ser recursiva.
    -No se debe usar [::-1] ni la función reversed().
"""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0].lower() == palabra[-1].lower():
        return es_palindromo(palabra[1:-1])
    else:
        return False

tildes = "áéíóúÁÉÍÓÚñÑ"
while True:
    tiene_espacios = False
    tiene_tildes = False
    try:
        palabra = str(input("\nIngrese una cadena de texto (Sin espacios ni tildes): "))
        for caracter in palabra:
            if caracter == " ":
                tiene_espacios = True
            if caracter in tildes:
                tiene_tildes = True
        if tiene_espacios or tiene_tildes:
            print("\nError. Ingrese una cadena de texto sin espacios ni tildes!")
        else:
            break
    except ValueError:
        print("\nError. Ingrese una cadena de texto!")

print()
if es_palindromo(palabra):
    print(f"La cadena de texto '{palabra}' es palindromo!")
else:
    print(f"La cadena de texto '{palabra}' NO es palindromo!")

