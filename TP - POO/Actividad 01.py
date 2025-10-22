class celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

    def __str__(self):
        return f"-Celda(Fila: {self.fila}, Columna: {self.columna}, Valor: '{self.valor}')"

class matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, celda):
        if not self.existe_posicion(celda.fila, celda.columna):
            self.celdasMatriz.append(celda)
            print("\nCelda agregada correctamente.")
            return True
        else:
            print(f"\nError. La posicion en la fila:'{celda.fila}', columna:'{celda.columna}' ya ha sido asignada en una celda anterior")
            return False
    
    def existe_posicion(self, fila, columna):
        for posicion in self.celdasMatriz:
            if posicion.fila == fila and posicion.columna == columna:
                return True
        
        return False
    
    def mostrar_celdas(self):
        if not self.celdasMatriz:
            print("\nLa matriz no tiene valores asignados!")
            return
        
        print("\nValores cargados en celdasMatriz")
        for celda in self.celdasMatriz:
            print(celda)
        print()

    def obtener_valor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
            
        return "La fila y columna indicada no han sido asignadas a ninguna celda!"

matriz = matriz()
print("\n-----Carga de valores en matriz-----")
print("Ingrese 'FIN' para salir")

while True:
    valor = input("\nIngrese el valor de la celda (o 'FIN' para salir): ")

    if valor.upper() == "FIN":
        print("\nSaliendo del estado de carga...")
        break
    try:
        print()
        fila = int(input("Ingrese el valor de 'fila' en la que lo quiere guardar: "))
        columna = int(input("Ingrese el valor de la 'columna' en la que lo quiere guardar: "))
    except ValueError:
        print("\nError. Los valores ingresados tienen que ser enteros!")
        continue

    nueva_celda = celda(fila,columna,valor)
    matriz.agregar_celda(nueva_celda)

matriz.mostrar_celdas()

if matriz.celdasMatriz:
    print("\nBuscar un valor:")
    try:
        buscar_fila = int(input("Ingrese la fila a buscar: "))
        buscar_columna = int(input("Ingrese la columna a buscar: "))
        resultado = matriz.obtener_valor(buscar_fila, buscar_columna)
        msj_error = "La fila y columna indicada no han sido asignadas a ninguna celda!"
        
        if resultado == msj_error:
            print(f"\n La fila:'{buscar_fila}' y la columna:'{buscar_columna}' no tienen ningun valor!")
        else:
            print(f"\n El valor en la fila:'{buscar_fila}' y en la columna:'{buscar_columna}' es: {resultado}")
    except ValueError:
        print("\nError. Ingrese un valor entero!")