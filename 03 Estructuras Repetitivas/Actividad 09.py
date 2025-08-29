cantidad = 0
suma = 0
media = 0

for i in range(0, 10, 1):
    num = int(input("Ingrese un numero:"))
    suma += num
    cantidad += 1
    
media = suma / cantidad
print("La media de los numeros es:", media)