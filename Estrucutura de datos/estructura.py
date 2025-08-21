#listas creacion
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
# listas acceso
print(lista[6])  # Acceso al primer elemento
#lista vacia
lista_vacia = []
# lista vacia voy a ingresar elementos
lista_vacia.append(1)  # Agregar un elemento a la lista vacía
print(lista_vacia)  # Imprimir la lista después de agregar 
# un elemento tipo texto
lista_vacia.append("Hola")  # Agregar un elemento a la lista vacía
print(lista_vacia)  # Imprimir la lista después de agregar un 
# insertar un boleano en la enmedio de 0 y 1
lista_vacia.insert(1, True)  # Insertar un elemento en la lista vacía
print(lista_vacia)  # Imprimir la lista después de insertar un elemento
#mostrar ultimo elemento de la lista
print(f"ultimo elemento de la lista es {lista_vacia[-1]}")  # Imprimir el último elemento de la lista
#mostrar longitud de la lista
print(f"cuantos elemento tiene la lista{len(lista_vacia)}")  # Imprimir la longitud de la lista
#eliminar un elemento de la lista
lista_vacia.remove(1)  # Eliminar un elemento de la lista de la psocicion indicada
# para que es pop() elimina el ultimo elemento de la lista
lista_vacia.pop()  # Eliminar el último elemento de la lista
print(lista_vacia)  # Imprimir la lista después de eliminar el último elemento
#modificar en una posicion especifica
#lista_vacia[0] = "Modificado"  # Modificar un elemento en una posición específica
print("\033[36m lista modificada",lista_vacia )  # Imprimir la :",lista_vacia)  # Imprimir la lista después de modificar un elemento
# extender lista
lista_vacia.extend([1, 2, 3])  # Extender la lista con una nueva lista
print("\033[35m Lista extendida:", lista_vacia, "\033[0m")
# listas de listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\033[32m Lista de listas:", lista_de_listas, "\033[0m")  # Imprimir la lista de listas
# Acceso a un elemento de una lista de listas   
print("\033[33m Elemento de la lista de listas:", lista_de_listas[1][2], "\033[0m")  # Imprimir un elemento específico de la lista de listas.
# llenar listas con valores aleatorios 
import random
lista_aleatoria = [random.randint(1, 100) for _  in range(10)]  # Lista con 10 números aleatorios entre 1 y 100
print("\033[34m Lista aleatoria:", lista_aleatoria, "\033[0m")  # Imprimir la lista aleatoria
# usando numpy para valores aleatorias en listas
import numpy as np
lista_numpy = np.random.randint(1, 100, size=10).tolist()# Lista con 10 números aleatorios entre 1 y 100 usando numpy
print("\033[31m Lista numpy aleatoria:", lista_numpy, "\033[0m")  # Imprimir la lista numpy aleatoria
# operacioens de la listas
lista_numpy.sort()  # Ordenar la lista numpy
print("\033[36m Lista numpy ordenada:", lista_numpy, "\033[0m")  # Imprimir la lista numpy ordenada
# invertir la lista
lista_numpy.reverse()  # Invertir la lista numpy
print("\033[35m Lista numpy invertida:", lista_numpy, "\033[0m")  # Imprimir la lista numpy invertida
# buscar un elemento en la lista    
print("\033[32m Buscar elemento en la lista numpy:", 30 in lista_numpy, "\033[0m")  # Buscar un elemento en la lista numpy
# buscar en la lista vacia
print("\033[33m Buscar elemento en la lista vacia:", 2 in lista_vacia, "\033[0m")  # Buscar un elemento en la lista vacía
# buscar pero con index
print("\033[34m Buscar elemento en la lista numpy:", lista_vacia.index(3), "\033[0m")  # Buscar un elemento en la lista vacía con index
# contar cuantas veces aparece un elemento en la lista
print("\033[31m Contar elemento en la lista numpy:", lista_numpy.count(50), "\033[0m")  # Contar cuantas veces aparece un elemento en la lista numpy
# copiar una lista
lista_copiada = lista_numpy.copy()  # Copiar la lista numpy
print("\033[36m Lista copiada:", lista_copiada, "\033[0m")  # Imprimir la lista copiada
# sumar dos listas
listaCopia=lista_numpy[:] # Copiar la lista numpy
print("\033[35m copia num:", listaCopia, "\033[0m")  # Imprimir la suma de dos listas
#limpiar lista
lista_numpy.clear()  # Limpiar la lista numpy
print("\033[32m Lista numpy limpia:", lista_numpy, "\033[0m")  # Imprimir la lista numpy limpia
# concatenar listas     
lista_concatenada = lista_vacia + lista_copiada  # Concatenar dos listas
print("\033[33m Lista concatenada:", lista_concatenada, "\033[0m")  
# sacar mayor valor de la lista
print("\033[34m Mayor valor de la lista copiada:", max(lista_copiada), "\033[0m")  # Imprimir el mayor valor de la lista copiada
# tamaño de la lista copiada
print("\033[31m Tamaño de la lista copiada:", len(lista_copiada), "\033[0m")  # Imprimir el tamaño de la lista copiada
