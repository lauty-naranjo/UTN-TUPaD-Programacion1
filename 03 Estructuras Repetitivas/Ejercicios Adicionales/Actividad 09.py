texto = input("Ingrese un texto: ")
consonantes = ""

for letra in texto:
    if (letra not in "aeiouAEIOU"):
          consonantes += letra

print(consonantes)