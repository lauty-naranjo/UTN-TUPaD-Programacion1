suma = 0
num = int(input("Ingrese un numero positivo:"))

while (num < 0):
    print("Incorrecto, ingrese un numero positivo")
    num = int(input("Ingrese un numero:"))

for i in range(0, num + 1, 1):
    suma += i

print("La suma de los numeros positivos es:", suma)