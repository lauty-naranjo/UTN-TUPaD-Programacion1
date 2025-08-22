"""

"""
# Actividad 1:

print ("Hola Mundo! \n");

# Actividad 2:

nombreP2 = input("Ingrese su nombre:")
print (f"Hola {nombreP2}!\n")

# Actividad 3:

nombreP3 = input("Ingrese su nombre:")
apellidoP3 = input("Ingrese su apellido:")
edadP3 = input("Ingrese su edad:")
residenciaP3 = input("Ingrese su residencia:")

print (f"Soy {nombreP3} {apellidoP3}, tengo {edadP3} años y vivo en {residenciaP3}. \n")

# Actividad 4:

radioP4 = float(input("Ingrese el radio de un circulo:"))
areaP4 = 3.14 * (radioP4**2)
perimetroP4 = 2 * 3.14 * radioP4

print (f"El área del circulo es: {areaP4}")
print (f"El perímetro del circulo es: {perimetroP4} \n")

# Actividad 5:

segundosP5 = int(input("Ingrese una cantidad de segundos: "))
horasP5 = segundosP5 / 3600

print (f"La cantidad de segundos convertidos en horas es de: {horasP5} horas \n")

# Actividad 6:

numeroP6 = int(input("Ingrese un numero: "))

print (f"{numeroP6} X 1 = ", numeroP6 * 1)
print (f"{numeroP6} X 2 = ", numeroP6 * 2)
print (f"{numeroP6} X 3 = ", numeroP6 * 3)
print (f"{numeroP6} X 4 = ", numeroP6 * 4)
print (f"{numeroP6} X 5 = ", numeroP6 * 5)
print (f"{numeroP6} X 6 = ", numeroP6 * 6)
print (f"{numeroP6} X 7 = ", numeroP6 * 7)
print (f"{numeroP6} X 8 = ", numeroP6 * 8)
print (f"{numeroP6} X 9 = ", numeroP6 * 9)
print (f"{numeroP6} X 10 = ", numeroP6 * 10, "\n")

# Actividad 7:

numero1_P7 = int(input("Ingrese un numero distinto a 0: "))
numero2_P7 = int(input("Ingrese otro numero distinto a 0: ")) 

print ("La suma de los numeros es: ", numero1_P7 + numero2_P7)
print ("La resta de los numeros es: ", numero1_P7 - numero2_P7)
print ("La multiplicacion de los numeros es: ", numero1_P7 * numero2_P7)
print ("La división los numeros es: ", numero1_P7 / numero2_P7, "\n")

# Actividad 8: 

pesoP8 = float(input("Ingrese su peso corporal: "))
alturaP8 = float(input("Ingrese su altura: "))

IMC = pesoP8 / (alturaP8 ** 2)

print(f"Su indice de masa corporal es de: {IMC} \n")

# Actividad 9:

tempCelsiusP9 = float(input("Ingrese la temperatura en grados Celsius:"))
tempFahrenheitP9 = (9/5 * tempCelsiusP9) + 32

print (f"La temperatura en grados Fahrenheit es de: {tempFahrenheitP9} \n")

# Actividad 10:

num1_P10 = int(input("Ingrese el primer numero:"))
num2_P10 = int(input("Ingrese el segundo numero:"))
num3_P10 = int(input("Ingrese el tercer numero:"))
suma_P10 = num1_P10 + num2_P10 + num3_P10
promedio_P10 = float(suma_P10/3)

print(f"El promedio de los 3 numeros ingresados es de: {promedio_P10} \n \n")

input("Escribe algo para terminar el programa:")