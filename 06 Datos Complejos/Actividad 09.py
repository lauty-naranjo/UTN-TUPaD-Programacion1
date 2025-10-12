#Funciones
def consultar_evento(agenda):
    dia = input("Ingrese el día (nombre del dia): ")
    hora = input("Ingrese la hora (formato HH:MM): ")
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"\nEvento el {dia} a las {hora}: {agenda[clave]}")
    else:
        print(f"\nNo hay eventos programados para {dia} a las {hora}.")

#Datos
agenda = {
    ("Lunes", "20:30"): "Clase de ingles",
    ("Martes", "08:00"): "Clase de Organizacion empresarial",
    ("Miercoles", "14:00"): "Trabajo",
    ("Jueves", "8:00"): "Clase de Programacion I",
    ("Viernes", "10:00"): "Reunion"
}

#Programa principal
opc = -1
while (opc != 0):
    print("\nMenú de opciones:")
    print("1. Consultar evento.")
    print("0. Salir.")

    opc = int(input("\nIngrese una opción: "))

    if (opc == 1):
        consultar_evento(agenda)
    elif (opc == 0):
        print("Saliendo del programa...")