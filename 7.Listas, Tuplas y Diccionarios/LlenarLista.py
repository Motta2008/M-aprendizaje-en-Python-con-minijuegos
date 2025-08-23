# juntar 2 listas
lista = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista + lista2
print(lista3)

#print("esta es una lista de distintos datos" + lista) # no se puede concatenar, no confundir unir 2 listas , a unir una lista a un string
print("esta es una lista de distintos datos", lista)

# como llenar una lista vacia

lista4 = [] # este tipo de procedimientos se hace con bucles 
# pero se puede hacer con una logica distinta 
edad = int(input("ingresa tu edad: "))
lista4.append(edad)
print(lista4)