"""
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
"""

def contar_bloques(num):
    if num == 1:
        return num
    else:
        return num + contar_bloques(num-1)

while True:
    try:
        num = int(input("\nIngrese el numero de bloques en el nivel mas bajo: "))
        if num >= 0:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

print()
print("Calculando la cantidad de bloques necesarios....")
print(f"La cantidad de bloques necesarios para una piramide con una base de {num} bloques es: ", contar_bloques(num))
