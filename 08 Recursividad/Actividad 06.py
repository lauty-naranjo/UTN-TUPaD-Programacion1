"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
"""

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)

while True:
    try:
        num = int(input("\nIngrese un numero a sumar sus digitos: "))
        if num >= 0:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

print()
print(f"La suma de los digitos del numero {num} es: ", suma_digitos(num))