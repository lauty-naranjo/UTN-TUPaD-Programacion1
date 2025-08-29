contador = 0
num = int(input("Ingrese un número entero: "))

while (num != 0):
    contador += 1
    num = num // 10

print("El número tiene", contador, "dígitos.")