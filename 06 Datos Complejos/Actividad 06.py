alumnos = {}
promedios = {}

promedio = 0

for i in range(3):
    nombre = input("\nIngrese el nombre del alumno: ")
    nota1 = -1
    nota2 = -1
    nota3 = -1

    while (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
        nota1 = int(input("Ingrese la nota 1 del alumno: "))
        nota2 = int(input("Ingrese la nota 2 del alumno: "))
        nota3 = int(input("Ingrese la nota 3 del alumno: "))
        if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
            print("\nError, las notas deben estar entre 0 y 10. Intente nuevamente.")

    notas =(nota1, nota2, nota3)
    alumnos[nombre] = notas

for nombres,notas in alumnos.items():
    promedio = sum(notas)/3
    promedios[nombres] = round(promedio,1)

print("\nAlumnos y sus notas:")
print(alumnos)

print("\nAlumnos y sus promedios:")
print(promedios)