import random
numAleatorio = random.randint(0, 9)

num = int(input("Adivine el numero:"))

while (num != numAleatorio):
    print("Incorrecto, intente de nuevo")
    num = int(input("Adivine el numero:"))

print("Correcto, el numero es:", numAleatorio)