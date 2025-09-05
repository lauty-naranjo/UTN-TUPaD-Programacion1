cadena = input("Ingrese una cadena de texto: ")
frecuencia = {}

palabras = cadena.split()

for palabra in palabras:
    if (palabra in frecuencia):
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(f"Frecuencia de palabras:{frecuencia}")