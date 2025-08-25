# se inicia con {}
# EL diccionario siempre tiene clave y valor
Diccionario = {'usuario' : "Michael" , 'contraseña' : 1234567}

print(Diccionario)
print(type(Diccionario))

# No se pueden tener claves duplicadas, nos mostrara la sustitucion del ultimo valor con el mismo nombre de clave
Diccionario = {'usuario' : "Michael" , 'contraseña' : 1234567, 'usuario' : "Motta"}
print(Diccionario)