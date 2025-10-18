"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""

def convertir(num):
    if num == 0:
        return ""
    else:
        return convertir(num // 2) + str(num % 2)
    
while True:
    try:
        num = int(input("\nIngrese un numero decimal:"))
        if num >= 0:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")
        
if num == 0:
    binario = "0"
else:
    binario = convertir(num)

print(f"El numero {num} convertido a binario es: {binario}")