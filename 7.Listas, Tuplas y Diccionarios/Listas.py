lista = ['Python', 7, 'Nombre', 3.14, 42.442] # las listas pueden ser homogeneas del mismo tipo o heterogeneas de diferente tipo de dato
print(type(lista)) #Type se coloca en los print si se quiere ver los tipos de datos que sea la palabra dentro del type

print("\033[32m Lista:", lista, "\033[0m") # Imprimir la lista

print(lista[3]) # Imprimir el elemento en la posición 3 de la lista

print(type(lista[3])) # Imprimir el tipo de dato del elemento en la posición 3 de la lista

print(len(lista)) # Imprimir la longitud de la lista

lista[0] = "PYTHON" # Modificar el primer elemento de la lista
print("\033[33m Lista modificada:", lista, "\033[0m")
