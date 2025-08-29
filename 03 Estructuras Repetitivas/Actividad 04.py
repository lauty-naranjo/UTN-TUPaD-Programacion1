num = int(input("Ingrese un número a sumar: "))
suma = num

while (num != 0):
    num = int(input("Ingrese otro número a sumar o 0 para terminar: "))
    suma += num

print("La suma total es:", suma)