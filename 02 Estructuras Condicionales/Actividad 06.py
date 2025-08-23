import random
from statistics import mode, median, mean  # Importa las funciones para calcular moda, mediana y media

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  # Genera 50 números aleatorios entre 1 y 100
print("Números aleatorios:", numeros_aleatorios, "\n")

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if (media > mediana and mediana > moda):
    print("Hay un sesgo positivo o la derecha")
elif (media < mediana and mediana < moda):
    print("Hay un sesgo negativo o la izquierda")
else: 
    print("No hay sesgo")