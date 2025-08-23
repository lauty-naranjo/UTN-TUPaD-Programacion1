palabra = input("Ingrese una palabra: ")

if (palabra[-1] in "aeiouAEIOU"):
    print(palabra + "!")
else:
    print(palabra)