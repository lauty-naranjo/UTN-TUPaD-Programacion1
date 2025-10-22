from Ingrediente import ingrediente
from Plato import plato

def main():
    platosMenu = []

    while True:
        print("\n--- Carga de nuevo plato ---")

        nombre_plato = input("Ingrese el nombre del plato/bebida (o ingrese FIN para salir): ")
        if nombre_plato.upper() == "FIN":
            break

        tipo_input = input("¿Es una bebida? (s/n): ")
        if tipo_input.lower() == 's':
            esBebida = True
        else:
            esBebida = False

        try:
            precio = float(input(f"Ingrese el precio de '{nombre_plato}': "))
        except ValueError:
            print("\nError. El precio debe ser un número. Intente de nuevo.")
            continue

        nuevo_plato = plato(nombre_plato, precio, esBebida)

        ingredientes_cargados = 0
        if not esBebida:
            print(f"\n--- Carga de ingrediente para '{nombre_plato}' ---")
            while True:
                nombre_ingrediente = input("Ingrese el nombre del ingrediente (o ingrese FIN para salir): ")
                if nombre_ingrediente.upper() == "FIN":
                    break

                try:
                    cantidad = float(input(f"Ingrese la cantidad de '{nombre_ingrediente}': "))
                except ValueError:
                    print("\nError. La cantidad debe ser un número. Intente de nuevo.\n")
                    continue

                unidad_de_medida = input(f"Ingrese la unidad de medida para '{nombre_ingrediente}': ")

                nuevo_ingrediente = ingrediente(nombre_ingrediente, cantidad, unidad_de_medida)
                nuevo_plato.agregarIngrediente(nuevo_ingrediente)
                ingredientes_cargados += 1
                print("\nIngrediente agregado correctamente.\n")

        if not esBebida and ingredientes_cargados == 0:
            print("\nError. Debe agregar al menos un ingrediente para un plato. Intente de nuevo.")
            continue

        platosMenu.append(nuevo_plato)
        print(f"\nEl Plato/Bebida '{nombre_plato}' agregado correctamente al menú.")

    print("\n-----------MENÚ-------------")

    if not platosMenu:
        print("No se han cargado platos o bebidas al menú.")
        return
    for platos in platosMenu:
        print(platos.mostrarInfo())
        print("---------------------")

main()