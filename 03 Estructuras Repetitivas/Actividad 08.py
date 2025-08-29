contador_positivos = 0
contador_negativos = 0
contador_pares = 0
contador_impares = 0

num = 0

for i in range(0, 100, 1):
    num = int(input("Ingrese un numero:"))

    if (num > 0):
        contador_positivos += 1
    elif (num < 0):
        contador_negativos += 1

    if (num % 2 == 0):
        contador_pares += 1
    else:
        contador_impares += 1

print("Cantidad de numeros positivos:", contador_positivos)
print("Cantidad de numeros negativos:", contador_negativos)
print("Cantidad de numeros pares:", contador_pares)
print("Cantidad de numeros impares:", contador_impares)