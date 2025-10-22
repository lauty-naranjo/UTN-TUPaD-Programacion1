from ComponentesCPU import componentesCPU
from Computadora import computadora

def main():
    print ("\n--- Carga de Computadora ---")

    while True:
        marca = input("Ingrese la marca de la computadora: ")
        modelo = input("Ingrese el modelo de la computadora: ")

        nueva_computadora = computadora(marca, modelo)

        while True:
            print("\n--- Carga de Componente/s ---")

            componente = input("Ingrese el nombre del componente (o ingrese FIN para salir): ")

            if componente.upper() == "FIN":
                break
            
            marca_componente = input("Ingrese la marca del componente: ")

            try:
                cantidad = int(input("Ingrese la cantidad del componente: "))
                precio = float(input("Ingrese el precio unitario del componente: "))
            except ValueError:
                print("\nError. La cantidad debe ser un número entero y el precio un número válido. Intente de nuevo.")
                continue

            nuevo_componente = componentesCPU(componente, marca_componente, cantidad, precio)
            nueva_computadora.agregar_componente(nuevo_componente)
            print(f"\nComponente '{componente}' agregado correctamente.\n")

        if not nueva_computadora.objetos_componentes:
            print("\nError. Debe agregar al menos un componente a la computadora. Intente de nuevo.")
            continue

        print("\n--- Informe de la Computadora ---")
        informe = nueva_computadora.generar_informe()
        print(f"\n{informe}")

        cotizar_otra = input("¿Desea cotizar otra computadora? (s/n): ")
        if cotizar_otra.lower() == "n":
            print("\n --- Fin del programa ---")
            break

main()