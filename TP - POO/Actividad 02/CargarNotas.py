from Nota import Nota
from Alumno import Alumno

def main():
    alumnos = []

    print("\n----Sistema de carga de alumnos:")
    while True:
        print("\nIngreso de datos del alumno")
        nombreCompleto = input(" -Ingrese el nombre completo del alumno: ")

        try:
            legajo = int(input(" -Ingrese el legajo del alumno: "))
        except ValueError:
            print("\nError. El legajo tiene que ser un numero entero!")
            continue

        nuevo_alumno = Alumno(nombreCompleto, legajo)

        notas_cargadas = 0
        print("\nCarga de notas del alumno: ")
        while True:
            nombreCatedra = input("\nIngrese el nombre de la catedra (o 'FIN' para salir): ")

            if nombreCatedra.upper() == "FIN":
                break

            try:
                notaExamen = float(input(f"Ingrese la nota para '{nombreCatedra}': "))
                if  notaExamen < 0 or notaExamen > 10:
                    print("\nNota fuera de rango! (0-10), Intente de nuevo.")
                    continue
            except ValueError:
                print("\nError. La nota tiene que ser un numero!")
                continue

            nueva_nota = Nota(nombreCatedra, notaExamen)
            nuevo_alumno.agregar_nota(nueva_nota)
            notas_cargadas += 1
            print("\nNota agregada correctamente.")

        if notas_cargadas == 0:
            print("\nError. Debe ingresar por lo menos una nota para el alumno!")
        else:
            alumnos.append(nuevo_alumno)
            print(f"\nAlumno:'{nombreCompleto}', Legajo:'{legajo}'. Se cargaron '{notas_cargadas}' notas correctamente.")

        salir = input("\nDesea cargar otro alumno? (S-N): ")
        if salir.upper() == "N":
            break
    
    print("\nInforme final de alumnos y promedios:\n")

    if not alumnos:
        print("\nNo hay alumnos cargados para generar informe.")
        return
    
    for alumno in alumnos:
        print(alumno)

        if alumno.lista_notas:
            print("\nNotas Cargadas:")

            for nota in alumno.lista_notas:
                print(nota)

        promedio = alumno.calcular_promedio()
        print(f"\nEl promedio del alumno es: {promedio}")
        print()

main()