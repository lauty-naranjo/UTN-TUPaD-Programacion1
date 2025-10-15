"""
Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"
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