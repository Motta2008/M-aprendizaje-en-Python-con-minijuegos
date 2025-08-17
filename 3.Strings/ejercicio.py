# Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

cadena = "Te quiero solo como amigo"

#imprima los dos primeros caracteres
print(cadena[0 : 2])

#imprima los tres ultimos caracteres
print(cadena[-3 : ])

# Imprima dicha cadena cada dos caracteres
print(cadena[: : 2]) # los dos puntos recorren toda la cadena, saca una copia y imprime los caracteres segun el numero asignado despues

# Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
print(cadena[: : -1]) # los dos puntos recorren toda la cadena, saca una copia y la imprime en sentido inverso por empezar con -1

#Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
print(cadena[0 : ] + cadena[: : -1]) # o print(cadena + cadena[::-1])
