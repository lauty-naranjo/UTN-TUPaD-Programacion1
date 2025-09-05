lista = []

for i in range (0,5):
    lista.append(int(input("Ingrese un numero: ")))

duplicados = [] 

for num in lista:
    if (lista.count(num) > 1 and num not in duplicados):
        duplicados.append(num)

print (f"Los numeros que se repiten son: {duplicados}")