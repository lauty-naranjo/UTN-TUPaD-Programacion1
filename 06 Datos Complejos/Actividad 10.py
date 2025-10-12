paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima",
    "Venezuela": "Caracas",
}

paises_invertido = {}

for pais, capital in paises.items():
    paises_invertido[capital] = pais

print("\nDiccionario original:\n")
for item in paises.items():
    print(item)
print("\nDiccionario invertido:\n")
for item in paises_invertido.items():
    print(item)