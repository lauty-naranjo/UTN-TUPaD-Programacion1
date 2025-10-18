"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""

def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
    
    if (numero % 10) == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return 0 + contar_digito(numero // 10, digito)


while True:
    try:
        numero = int(input("\nIngrese un numero entero:"))
        if numero >= 0:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError. Ingrese un numero entero!")

while True:
    try:
        digito = int(input("\nIngrese un digito entre (0 - 9):"))
        if 9 >= digito >= 0 :
            break
        else:
            print("\nError. Ingrese un numero entre (0 - 9)!")
    except ValueError:
        print("\nError. Ingrese un numero entero!")

if numero == 0 and digito == 0:
    resultado = 1
else:
    resultado = contar_digito(numero, digito)

print()
print(f"El numero '{digito}' aparece {resultado} veces en '{numero}'")