num = int(input("Ingrese un numero positivo: "))

while (num <= 0):
    num = int(input("Ingrese un numero positivo: "))

for i in range(2, num+1):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if (i % j == 0):
            es_primo = False
            break
    if (es_primo):
        print(i, end=" ")

