#Funciones
def consultar_stock(productos):
    print("\nStock actual de productos:")
    for producto, cantidad in productos.items():
        print(f"{producto}: {cantidad} unidades")

def agregar_unidades(productos):
    producto = input("Ingrese el nombre del producto a agregar unidades: ")
    if producto in productos:
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        productos[producto] += unidades
        print(f"Se agregaron {unidades} unidades a {producto}. stock actualizado: {productos[producto]} unidades")
    else:
        print("\nEl producto no existe en el inventario!")

def agregar_producto(productos):
    producto = input("Ingrese el nombre del nuevo producto: ")
    if producto not in productos:
        unidades = int(input("Ingrese la cantidad inicial de unidades: "))
        productos[producto] = unidades
        print(f"Producto {producto} agregado con {unidades} unidades.")
    else:
        print("\nEl producto ya existe en el inventario!")

#Datos
productos = {
    "Banana": 12, 
    "Ananá": 10, 
    "Melón": 10, 
    "Uva": 15
    }

#Programa principal
opc = -1
while (opc != 0):
    print("\nMenú de opciones:")
    print("1. Consultar stock.")
    print("2. Agregar unidades.")
    print("3. Agregar producto.")
    print("0. Salir.")

    opc = int(input("\nIngrese una opción: "))

    if (opc == 1):
        consultar_stock(productos)
    elif (opc == 2):
        agregar_unidades(productos)
    elif (opc == 3):
        agregar_producto(productos)
    elif (opc == 0):
        print("Saliendo del programa...")
