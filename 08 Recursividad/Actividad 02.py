"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
while True:
    try:
        num = int(input("\nIngrese un numero a calcular su serie Fibonacci:"))
        if num >= 1:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

print(f"\nLa serie Fibonacci hasta el numero '{num}' es:", end = " ")
for i in range(num+1):
    print(fibonacci(i), end= " ")
print()