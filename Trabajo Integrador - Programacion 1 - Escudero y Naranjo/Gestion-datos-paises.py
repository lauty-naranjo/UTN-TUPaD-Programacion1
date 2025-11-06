# ===========================================
# GESTIÓN DE DATOS DE PAÍSES
# Trabajo Práctico Integrador
# Lautaro Naranjo y Martin Escudero :)
# ===========================================

import csv
import locale

# Configurar formato numérico local
locale.setlocale(locale.LC_ALL, "")

# Colores ANSI para mejorar la vista
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"


# -------------------------------------------
# Función auxiliar para formato latino
# -------------------------------------------
def formatear_numero(num):
    return f"{num:,}".replace(",", ".")  # puntos como separador de miles


# -------------------------------------------
# Cargar datos desde CSV
# -------------------------------------------
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"],
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"{RED}Fila ignorada por datos inválidos:{RESET} {fila}")
    except FileNotFoundError:
        print(f"{RED}Archivo CSV no encontrado.{RESET}")
    return paises


# -------------------------------------------
# Funciones de búsqueda y filtrado
# -------------------------------------------
def buscar_pais(paises, nombre_busqueda):
    return [p for p in paises if nombre_busqueda.lower() in p["nombre"].lower()]


def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_rango_poblacion(paises, min_pob, max_pob):
    return [p for p in paises if min_pob <= p["poblacion"] <= max_pob]


def filtrar_por_rango_superficie(paises, min_sup, max_sup):
    return [p for p in paises if min_sup <= p["superficie"] <= max_sup]


# -------------------------------------------
# Función para mostrar países en formato tabla
# -------------------------------------------
def mostrar_tabla_paises(paises):
    if not paises:
        print(f"{RED}No hay países para mostrar.{RESET}")
        return

    print(
        f"\n{BOLD}País{' ' * 22}Población{' ' * 4}Superficie (km²){' ' * 5}Continente{RESET}"
    )
    print("-" * 75)
    for p in paises:
        print(
            f"{p['nombre']:<25}{formatear_numero(p['poblacion']):>12}{formatear_numero(p['superficie']):>18}{p['continente']:>15}"
        )
    print("-" * 75)


# -------------------------------------------
# Función de ordenamiento
# -------------------------------------------
def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


# -------------------------------------------
# Funciones de estadísticas
# -------------------------------------------
def estadisticas(paises):
    if not paises:
        print(f"{RED}No hay datos para mostrar estadísticas.{RESET}")
        return

    mayor_pob = max(paises, key=lambda x: x["poblacion"])
    menor_pob = min(paises, key=lambda x: x["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    conteo_continente = {}
    for p in paises:
        cont = p["continente"]
        conteo_continente[cont] = conteo_continente.get(cont, 0) + 1

    print(f"\n{BOLD}{CYAN}=== ESTADÍSTICAS GENERALES ==={RESET}")
    print(
        f"{YELLOW}País con mayor población:{RESET} {mayor_pob['nombre']} ({formatear_numero(mayor_pob['poblacion'])} habitantes)"
    )
    print(
        f"{YELLOW}País con menor población:{RESET} {menor_pob['nombre']} ({formatear_numero(menor_pob['poblacion'])} habitantes)"
    )
    print(
        f"{YELLOW}Promedio de población:{RESET} {formatear_numero(round(promedio_pob))} habitantes"
    )
    print(
        f"{YELLOW}Promedio de superficie:{RESET} {formatear_numero(round(promedio_sup))} km²"
    )
    print(f"{YELLOW}Cantidad de países por continente:{RESET}")
    for cont, cant in conteo_continente.items():
        print(f"  - {cont}: {cant}")
    print(f"{CYAN}==================================\n{RESET}")


# -------------------------------------------
# Menú interactivo
# -------------------------------------------
def mostrar_menu():
    print(f"\n{BOLD}{CYAN}=================================={RESET}")
    print(f"{BOLD}{CYAN}      MENÚ DE GESTIÓN DE PAÍSES   {RESET}")
    print(f"{BOLD}{CYAN}=================================={RESET}")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")


# -------------------------------------------
# Programa principal
# -------------------------------------------
def main():
    paises = cargar_paises("paises.csv")

    if not paises:
        print(f"{RED}No se cargaron datos. Saliendo...{RESET}")
        return

    while True:
        mostrar_menu()
        try:
            opcion = int(input(f"\n{BOLD}Ingrese una opción:{RESET} "))
        except ValueError:
            print(f"{RED}Opción inválida. Debe ingresar un número del 1 al 7.{RESET}")
            continue

        print(f"\n{CYAN}-------------------------------------------{RESET}")

        if opcion == 1:
            nombre = input("Ingrese nombre o parte del nombre del país: ")
            resultados = buscar_pais(paises, nombre)
            if resultados:
                mostrar_tabla_paises(resultados)
            else:
                print(f"{RED}No se encontraron países.{RESET}")

        elif opcion == 2:
            cont = input("Ingrese continente: ")
            filtrados = filtrar_por_continente(paises, cont)
            if filtrados:
                mostrar_tabla_paises(filtrados)
            else:
                print(f"{RED}No hay países en ese continente.{RESET}")

        elif opcion == 3:
            try:
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                filtrados = filtrar_por_rango_poblacion(paises, min_p, max_p)
                if filtrados:
                    mostrar_tabla_paises(filtrados)
                else:
                    print(
                        f"{RED}No hay países dentro de ese rango de población.{RESET}"
                    )
            except ValueError:
                print(f"{RED}Ingrese números válidos.{RESET}")

        elif opcion == 4:
            try:
                min_s = int(input("Superficie mínima: "))
                max_s = int(input("Superficie máxima: "))
                filtrados = filtrar_por_rango_superficie(paises, min_s, max_s)
                if filtrados:
                    mostrar_tabla_paises(filtrados)
                else:
                    print(
                        f"{RED}No hay países dentro de ese rango de superficie.{RESET}"
                    )
            except ValueError:
                print(f"{RED}Ingrese números válidos.{RESET}")

        elif opcion == 5:
            clave = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            orden = input("Ascendente o descendente? (a/d): ").lower()
            descendente = True if orden == "d" else False
            paises_ordenados = ordenar_paises(paises, clave, descendente)
            print(f"\n{CYAN}Listado ordenado:{RESET}")
            mostrar_tabla_paises(paises_ordenados)

        elif opcion == 6:
            estadisticas(paises)

        elif opcion == 7:
            print(f"\n{YELLOW}Saliendo del programa... ¡Hasta luego!{RESET}\n")
            break

        else:
            print(f"{RED}Opción inválida. Intente nuevamente.{RESET}")

        print(f"{CYAN}----------------------------------{RESET}")


if __name__ == "__main__":
    main()
