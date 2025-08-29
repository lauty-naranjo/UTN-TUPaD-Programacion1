valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0

if (valor1 > valor2):
    while (valor1 -1 > valor2):
        valor1 -= 1
        suma += valor1
        print (suma)
else:
    while (valor1 + 1< valor2):
        valor1 += 1
        suma += valor1
        print (suma)

print("La suma de los números enteros entre los dos valores es:", suma)