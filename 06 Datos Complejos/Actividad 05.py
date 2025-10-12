frase = input("Ingrese una frase:")
frase_minusculas = frase.lower()
palabras = frase_minusculas.split()

palabras_unicas = set(palabras)
recuentro = {}

for palabra in palabras:
    if palabra in recuentro:
        recuentro[palabra] += 1
    else:
        recuentro[palabra] = 1

print(recuentro)