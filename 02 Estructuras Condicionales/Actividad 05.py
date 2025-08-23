contraseña = input("Ingrese la contraseña: ")

if (len(contraseña) <= 14 and len(contraseña) >= 8):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")