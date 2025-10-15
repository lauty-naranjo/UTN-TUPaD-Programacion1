legajo_alumnos = {}

#Funciones
def leer_alumnos(legajo_alumnos):
    try:
        with open("alumnos.txt", "r") as archivo:
            legajo_alumnos.clear()
            for linea in archivo:
                linea_limpia = linea.strip()
                nombre, apellido, legajo, notapromedio = linea_limpia.split(';')
                legajo = int(legajo)
                notapromedio = float(notapromedio)

                alumno = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "promedio": notapromedio
                }
                legajo_alumnos[legajo] = alumno
    except:
        print("Error de la lectura del archivo: 'alumnos.txt'.")

def ver_alumnos(legajo_alumnos):
    print("\n----Listado de Alumnos----\n")
    for legajo, datos in legajo_alumnos.items():
       print(f"Legajo: {legajo} | Nombre: {datos['nombre']} {datos['apellido']} | Promedio: {datos['promedio']}")
    print()

def validar_si_existe(legajo, legajo_alumnos):
    return legajo in legajo_alumnos

def validar_nombre_o_apellido(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isalpha():
            return valor
        else:
            print("Error: Ingrese un valor valido!")

def validar_legajo(legajo_alumnos):
    while True:
        legajo = input("\nIngrese el legajo del alumno (5 digitos): ")
        if legajo.isdigit() and len(legajo) == 5:
            nuevo_legajo = int(legajo)
            if validar_si_existe(nuevo_legajo, legajo_alumnos):
                print(f"\nError: El legajo {nuevo_legajo} ya existe en el archivo.")
            else:
                return nuevo_legajo
        else:
            print("\nError: Ingrese un valor numérico y de 5 digitos para el legajo.")

def validar_promedio():
    while True:
        nuevo_promedio = input("\nIngrese el promedio del alumno: ")
        try:
            nuevo_promedio = float(nuevo_promedio)
            if 0 <= nuevo_promedio <= 10:
                return nuevo_promedio
            else:
                print("\nError: Ingrese un promedio entre 0 y 10.")
        except ValueError:
            print("\nError: Ingrese un valor numérico para el promedio.")

def agregar_alumno(legajo_alumnos):
    print("\n----Agregar un nuevo alumno----\n")
    nuevo_nombre = validar_nombre_o_apellido("Ingrese el nombre del alumno: ")
    nuevo_apellido = validar_nombre_o_apellido("Ingrese el apellido del alumno: ")
    nuevo_legajo = validar_legajo(legajo_alumnos)
    nuevo_promedio = validar_promedio()

    nuevo_alumno = {
        "nombre": nuevo_nombre,
        "apellido": nuevo_apellido,
        "promedio": nuevo_promedio
    }
    legajo_alumnos[nuevo_legajo] = nuevo_alumno

    linea = f"{nuevo_nombre};{nuevo_apellido};{nuevo_legajo};{nuevo_promedio}\n"
    try:
        with open("alumnos.txt", "a") as archivo:
            archivo.write(linea)
            print(f"\nAlumno '{nuevo_nombre} {nuevo_apellido}' agregado exitosamente.")
    except:
        print("Error al escribir en el archivo: 'alumnos.txt'.")

def guardar_aprobados(legajo_alumnos):
    try:
        with open("aprobados.txt", "w") as archivo:
            alumnos_aprobados = False
            for legajo, datos in legajo_alumnos.items():
                if datos['promedio'] >= 6:
                    linea = f"{datos['nombre']};{datos['apellido']};{legajo};{datos['promedio']}\n"
                    archivo.write(linea)
                    alumnos_aprobados = True
    except:
        print("Error de escritura al generar 'aprobados.txt'.")

    print("\n----Listado de Aprobados----\n")

    if not alumnos_aprobados:
        print("No hay alumnos aprobados!")
        return
    
    try:
        with open("aprobados.txt", "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()

                nombre, apellido, legajo, notapromedio = linea_limpia.split(';')
                legajo = int(legajo)
                notapromedio = float(notapromedio)

                print(f"Legajo: {legajo} | Nombre: {nombre} {apellido} | Promedio: {notapromedio}")
    except:
        print("Error al leer el archivo: 'aprobados.txt'.")

#Programa principal
leer_alumnos(legajo_alumnos)

opc = 0
while opc != 4:
    print("---- Menú ----")
    print("1. Ver alumnos")
    print("2. Agregar un alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")

    while True:
        opc = (input("Ingrese una opción: "))
        if opc.isdigit():
            opc = int(opc)
            if 5 > opc > 0:
                break
            else:
                print("\nError: Opción inválida. Intente nuevamente.\n")
        else:
            print("\nError: Opción inválida. Intente nuevamente.\n")

    if opc == 1:
        ver_alumnos(legajo_alumnos)

    elif opc == 2:
        agregar_alumno(legajo_alumnos)

    elif opc == 3:
        guardar_aprobados(legajo_alumnos)

    elif opc == 4:
        print("\nSaliendo del programa...")