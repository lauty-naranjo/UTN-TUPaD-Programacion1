"""
Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista.
"""
ruta = "d:/Programacion I/programacion1_trabajos/07 Manejo de archivos/productos.txt"
productos = []

#Funciones
def cargar_productos(ruta, productos):
    with open(ruta, "r") as archivo:
        productos.clear()
        for linea in archivo:
            linea_limpia = linea.strip()
            nombre, precio, cantidad = linea_limpia.split(',')
            precio = int(precio)
            cantidad = int(cantidad)

            productos_dicc = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(productos_dicc)

def mostrar_productos(productos):
    print("\n----Listado de Productos----\n")
    for producto in productos:
        print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")

def agregar_producto(productos):
    print("\n----Agregar un nuevo producto----\n")
    nuevo_nombre = input("Ingrese el nombre del producto: ")
    while True:
        nuevo_precio = input("Ingrese el precio del producto: ")
        if nuevo_precio.isdigit():
            nuevo_precio = int(nuevo_precio)
            break
        else:
            print("Error: Ingrese un valor numérico para el precio.")
    while True:
        nueva_cantidad = input("Ingrese la cantidad del producto: ")
        if nueva_cantidad.isdigit():
            nueva_cantidad = int(nueva_cantidad)
            break
        else:
            print("Error: Ingrese un valor numérico para la cantidad.")

    nuevo_producto = {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "cantidad": nueva_cantidad
    }
    productos.append(nuevo_producto)
    print(f"\nProducto '{nuevo_nombre}' agregado exitosamente.")

def buscar_producto(productos):
    producto_buscado = input("\nIngrese el nombre del producto a buscar: ")

    for producto in productos:
        if producto["nombre"].lower() == producto_buscado.lower():
            print("\nProducto encontrado!")
            print(f" -Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")
            break
    else:
        print(f"\nEl producto '{producto_buscado}' no existe en el inventario.")

def sobrescribir_archivo(ruta, productos):
    with open(ruta, "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("\nArchivo sobrescrito con los productos actualizados.")

#Programa principal
cargar_productos(ruta, productos)

opc = -1
while opc != 0:
    print("\n----Menú de opciones----\n")
    print("1. Mostrar productos")
    print("2. Agregar un nuevo producto")
    print("3. Buscar un producto")
    print("4. Sobrescribir archivo con productos actualizados")
    print("0. Salir")
    while True:
        opc = (input("Ingrese una opción: "))
        if opc.isdigit():
            opc = int(opc)
            if 5 > opc > -1:
                break
            else:
                print("\nError: Opción inválida. Intente nuevamente.\n")
        else:
            print("\nError: Opción inválida. Intente nuevamente.\n")

    if opc == 1:
        mostrar_productos(productos)

    elif opc == 2:
        agregar_producto(productos)

    elif opc == 3:
        buscar_producto(productos)

    elif opc == 4:
        sobrescribir_archivo(ruta, productos)

    elif opc == 0:
        print("\nSaliendo del programa...")