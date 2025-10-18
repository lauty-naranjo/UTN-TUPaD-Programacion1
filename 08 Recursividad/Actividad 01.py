"""
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    
while True:
    try:
        num = int(input("\nIngrese un numero a calcular su factorial y sus anteriores:"))
        if num >= 1:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

print()
for i in range(1, num + 1):
    print(f"El factorial de: {i} es: ", factorial(i))