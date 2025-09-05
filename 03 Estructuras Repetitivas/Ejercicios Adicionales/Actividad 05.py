cont = 0
cadena = str(input("Ingrese una cadena de texto: "))

for i in range(0, len(cadena)):
    if (cadena[i] in "aeiouAEIOU"):
        cont += 1

print (f"La cantidad de vocales en la cadena es: {cont}")