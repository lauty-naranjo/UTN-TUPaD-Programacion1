"""
Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad. 
"""

ruta = "d:/Programacion I/programacion1_trabajos/07 Manejo de archivos/productos.txt"

productos = []

with open(ruta, "r") as archivo:
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

print()
for linea in productos:
    print(linea['nombre'], "-", linea['precio'], "-", linea['cantidad'])
