from Barrio import barrio
from Vivienda import vivienda
from Habitacion import habitacion

def main():
    
    print("\n--- Carga de Barrio ---")
    while True:

        nombre_barrio = input("Ingrese el nombre del barrio: (o FIN para salir): ")
        if nombre_barrio.upper() == "FIN":
            break

        empresa_constructora = input("Ingrese el nombre de la empresa constructora: ")

        nuevo_barrio = barrio(nombre_barrio, empresa_constructora)

        print("\n--- Carga de Vivienda ---")
        while True:

            manzana = input("Ingrese la manzana de la vivienda (o ingrese FIN para salir): ")
            if manzana.upper() == "FIN":
                break

            calle = input("Ingrese la calle de la vivienda: ")

            try:
                numero = int(input("Ingrese el número de la vivienda: "))
                nroCasa = int(input("Ingrese el número de casa: "))
                superficieTerreno = float(input("Ingrese la superficie del terreno (m2): "))

                if superficieTerreno <= 0:
                    print("\nError. La superficie del terreno debe ser un número positivo. Intente de nuevo.")
                    continue

            except ValueError:
                print("\nError. Los valores numéricos ingresados no son válidos. Intente de nuevo.\n")
                continue

            nueva_vivienda = vivienda(calle, numero, manzana, nroCasa, superficieTerreno)

            print("\n--- Carga de Habitaciones ---")
            num_habitaciones = 0
            while True:

                nombre_habitacion = input("Ingrese el nombre de la habitación (o ingrese FIN para salir): ")
                if nombre_habitacion.upper() == "FIN":
                    break

                try:
                    metrosCuadrados = float(input(f"Ingrese los metros cuadrados de la habitacion '{nombre_habitacion}': "))

                    if metrosCuadrados <= 0:
                        print("\nError. Los metros cuadrados deben ser un número positivo. Intente de nuevo.")
                        continue

                except ValueError:
                    print("\nError. Los metros cuadrados deben ser un número válido. Intente de nuevo.")
                    continue

                nueva_vivienda.agregar_habitacion(habitacion(nombre_habitacion, metrosCuadrados))
                num_habitaciones += 1
                print(f"\nHabitación '{nombre_habitacion}' agregada correctamente.\n")

            if num_habitaciones == 0:
                print("\nError. Debe agregar al menos una habitación a la vivienda. Intente de nuevo.")
                continue

            nuevo_barrio.agregar_vivienda(nueva_vivienda)
            print("\nVivienda agregada correctamente al barrio.\n")

        if not nuevo_barrio.listaViviendas:
            print("\nNo se han agregado viviendas al barrio. Fin del programa.")
            return

        print("\n--- Informe del Barrio ---")
        print(f"Barrio: {nuevo_barrio.nombre}")
        print(f"Empresa Constructora: {nuevo_barrio.empresaConstructora}\n")

        print(f"Superficie Total del Terreno: {nuevo_barrio.getSuperficieTotalTerreno()} m2")
        print(f"Superficie Total Cubierta: {nuevo_barrio.getSuperficieTotalCubierta()} m2")

        manzana_consulta = input("\nIngrese la manzana para consultar su superficie total del terreno: ")
        superficie_manzana = nuevo_barrio.getSuperficieTotalTerrenoXManzana(manzana_consulta)
        print(f"Superficie Total del Terreno en la Manzana '{manzana_consulta}' es: {superficie_manzana} m2")
        
        cargar_otro = input("\n¿Desea cargar otro barrio? (s/n): ")
        if cargar_otro.lower() == "n":
            print("\n --- Fin del programa ---")
            break

main()
