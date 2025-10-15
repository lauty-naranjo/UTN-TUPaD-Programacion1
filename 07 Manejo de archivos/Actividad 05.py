"""
Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error. 
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

producto_buscado = input("Ingrese el nombre del producto a buscar: ")

for producto in productos:
    if producto["nombre"].lower() == producto_buscado.lower():
        print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")
        break
else:
    print(f"El producto '{producto_buscado}' no existe en el inventario.")
        
