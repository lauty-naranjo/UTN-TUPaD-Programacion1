nombre = input("Ingrese su nombre: ")

print ("Ingrese una opción:")
print ("1. Nombre en mayusculas")
print ("2. Nombre en minusculas")
print ("3. Nombre con la primera letra en mayuscula")

opcion = input("Ingrese una opción (1, 2 o 3): ")

if (opcion == "1"):
    print (nombre.upper())
elif (opcion == "2"):
    print (nombre.lower())
elif (opcion == "3"):
    print (nombre.title())
else:
    print ("Ingrese una opción válida")