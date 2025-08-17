#Format
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# se concatena con , ya que no son str ambos datos

print("Hola {} tienes {} años".format(nombre, edad)) # es similar a una lista, imprme los datos de las variables en los corchetes {} segun el orden de variables que esten en ,format