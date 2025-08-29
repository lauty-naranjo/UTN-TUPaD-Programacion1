num = int(input("Ingrese un numero:"))
invertido = 0
digito = 0

while (num != 0):
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print("El numero invertido es:", invertido)