contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    contactos[nombre] = telefono

print("")
consulta = input("Ingrese el nombre del contacto a buscar: ")
if consulta in contactos:
    print(f"El teléfono de {consulta} es {contactos[consulta]}")
else:
    print(f"No se encontró el contacto {consulta}")