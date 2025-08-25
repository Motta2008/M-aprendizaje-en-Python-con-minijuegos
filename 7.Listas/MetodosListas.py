# ¿com agregar un objeto a una lista? con el metodo append
lista = [1, 2, 3, 4, 5, 2, 2, 1]

print(lista)
 #nombre de lista + .append
lista.append(7)
print(lista)

lista.append('python')
print(lista)

# si queremos agregar un dato en un orden especifico de la lista
# insert
lista.insert(2, 2.5) # el 2 es la posicion y luego se inserta el valor del dato
print(lista)


# contar cuantos objetos hay en la lista con el valor dento del ()
print(lista.count(2))

# index, va a recibir un parametro y buscara en que poscion esta el primer valor que tenga el parametro, pr ejemplo, si hay varios 2 en la lista, buscara el primer 2 y devolvera la ubicacion
print(lista.index(2))

# si queremos ordenar una lista, usa el metodo sort
#no lleva parametro
#se hace por aparte no dentro del print
# no funciona si la lista no tiene los mismos tipos de datos
listasort = [1, 2, 3, 4, 5, 1,2, 5, 3,2]
listasort.sort()
print(listasort)

#actualizar datos dentro de la misma o sustituir
lista3 = ['python', 7, 'michael', 'Motta', 3]
# vamos a corregir el str michael ya que por gramatica debe iniciar en mayuscula 
#ubicar la posicion del dato
lista3[2] = 'Michael'
print(lista3)

# si queremos eliminar un dato de la lista
lista3.remove(7)
print(lista3)
#con metodo pop
lista3.pop() # toma el ultimo valor de la lista y lo elimina
print(lista3)
# si queremos eliminar un dato en una posicion especifica
lista3.pop(0) # elimina el elemento en la posicion 0
print(lista3)

# ambos son muy diferente
#remove elimina el parametro(valor) dentro de la lista, lo posiciona y lo elimina 
# pop elimina el elemento en la posicion que le digamos, si no le decimos nada elimina el ultimo 



