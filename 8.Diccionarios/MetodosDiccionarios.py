Diccionario = {1 : 2 , 2 :3 , 3 : 4}
print(Diccionario)

# El pop en Diccionarios recibe como parametro una clave y la elimina
Diccionario.pop(1)
print(Diccionario)

# limpiar el Diccionario
Diccionario.clear()
print(Diccionario)

# get nos devolvera un valor, recibe el parametro de la llave
Diccionario.get(1) # Nos devolvera None porque el diccionario esta vacio por el clear

# setdefault, recibe el valor de llave y su valor
Diccionario.setdefault(7 , 3)
print(Diccionario)

# update, actualizar el valor de los 2 diccionarios, se juntan, y si en dado caso hay una llave repetida el valor se hace una sola
Diccionario2 = {4: 5, 6: 7}
Diccionario.update(Diccionario2)
print(Diccionario)

# saca una copia, va sin parametro
Diccionario2.copy()
print(Diccionario2)
