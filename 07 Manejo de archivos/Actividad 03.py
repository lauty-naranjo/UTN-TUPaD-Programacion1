"""
Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente. 
"""

ruta = "d:/Programacion I/programacion1_trabajos/07 Manejo de archivos/productos.txt"

with open(ruta, "r") as archivo:
    print("\n----Listado de Productos----\n")
    for linea in archivo:
        linea_limpia = linea.strip()
        nombre, precio, cantidad = linea_limpia.split(',')
        precio = int(precio)
        cantidad = int(cantidad)
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

with open(ruta, "a") as archivo:
    print("\n----Agregar un nuevo producto----\n")
    nuevo_nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = input("Ingrese el precio del producto: ")
    nueva_cantidad = input("Ingrese la cantidad del producto: ")
    archivo.write(f"\n{nuevo_nombre},{nuevo_precio},{nueva_cantidad}")
    print(f"\nProducto '{nuevo_nombre}' agregado exitosamente.")