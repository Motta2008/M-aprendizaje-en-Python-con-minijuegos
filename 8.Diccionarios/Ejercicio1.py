# En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

capitales = {
    'Colombia': 'Bogotá',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Perú': 'Lima',
    'Venezuela': 'Caracas',
    'Ecuador': 'Quito',
    'Bolivia': 'Sucre',
    'Paraguay': 'Asunción',
    'Uruguay': 'Montevideo',
    'Guyana': 'Georgetown',
    'Surinam': 'Paramaribo',
    'Guayana Francesa': 'Cayena',
}

pais = input("ingrese un pais para ver su capital, *Respete mayusculas y acentos:")

print(capitales.get(pais, "No se encuentra el pais en el diccionario")) 

# or 

pais = input("ingrese un pais para ver su capital, *Respete mayusculas y acentos: ")

letra = pais.capitalize() in capitales # capitalize para ver si esa en mayuscula la rimera letra en diccionario

if letra  == True:
    print(capitales[pais .capitalize() ])
else:
    print("No se encuentra el pais en el diccionario")

# or

if pais.capitalize( ) in capitales:
    print(capitales[pais.capitalize()])
else:
    print("No se encuentra el pais en el diccionario")