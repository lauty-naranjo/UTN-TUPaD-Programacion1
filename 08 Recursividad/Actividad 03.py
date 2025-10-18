"""
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛(𝑚) = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un
algoritmo general.
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base* potencia(base, exponente-1)

while True:
    try:
        base = int(input("\nIngrese la base:"))
        if base >= 1:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

while True:
    try:
        exponente = int(input("\nIngrese el exponente:"))
        if exponente >= 0:
            break
        else:
            print("\nError. Ingrese un numero positivo!")
    except ValueError:
        print("\nError.Ingrese un numero entero!")

print()
print(f"El resultado de base {base} esponente {exponente} es: ", potencia(base,exponente))