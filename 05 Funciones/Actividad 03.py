"""
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
#Funcion
def informacion_personal(nombre, apellido, edad, resindencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {resindencia}.")


# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
resindencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, resindencia)