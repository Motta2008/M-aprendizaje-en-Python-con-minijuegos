# las tuplas no se puede modificar despues de creada
# las tuplas son inmutables, no se pueden modificar una vez creadas
""" las listas se crean con [], las tuplas con ()   """
tupla = (1, 2, 3, 4, 5)  # Crear una tupla
print("\033[32m Tupla:", tupla, "\033[0m")
#operaciones de las tuplas
print("\033[33m Longitud de la tupla:", len(tupla), "\033[0m")  # Imprimir la longitud de la tupla
print("\033[34m Primer elemento de la tupla:", tupla[0], "\033[0m")  # Imprimir el primer elemento de la tupla
print("\033[35m Último elemento de la tupla:", tupla[-1], "\033[0m")  # Imprimir el último elemento de la tupla
# buscar un elemento 
print("\033[36m Buscar elemento en la tupla:", 3 in tupla, "\033[0m")  # Buscar un elemento en la tupla
#otra forma usando index
print("\033[37m Buscar elemento en la tupla:", tupla.index(3), "\033[0m")  # Buscar un elemento en la tupla usando index