# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
# si es menor de 3 caracteres no es valida
p1 = input("Escribe una plabara que rime con la segunda palabra que escribiras: ")
p2 = input("Escribe una segunda palabra:")

# if p1 == p2[ : -3]: # Mí error fe que al iniciar en 0 va desde el primer caracter de comilla y no desde el ultimo caracter y termina hasta el caracter -3 contando los primeros caracteres y no los ultimos
#     print("las palabras riman")
# elif p1 == p2[ : -2]:
#     print("Las palabras riman un poco")
# else:
#     print("Las palabras no riman") (Mí solucion, esta mala)

if len(p1) < 3 or len(p2) <3: # len para contar el numero de caracteres
    print("No rima ya que no cumple los caracteres minimos")
elif p1[-3: ] == p2[-3: ]:
    print("las palabras riman")
elif p1[-2 : ] == p2[-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")

