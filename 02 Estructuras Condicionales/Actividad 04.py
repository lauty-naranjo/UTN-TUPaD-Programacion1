edad = int(input("Ingrese su edad:"))

if (edad < 12):
    print("Eres un niño")
elif (edad >= 12 and edad < 18):
    print("Eres un adolescente")
elif (edad >= 18 and edad < 30):
    print("Eres un adulto joven")
else:
    print("Eres un adulto")