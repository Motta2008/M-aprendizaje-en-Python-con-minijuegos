Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Multiplicacion = 2

# print(Numeros[4, 7, 9] * Multiplicacion)  # Esto no es correcto, no se puede multiplicar una lista directamente
print([Numeros[4], Numeros[7], Numeros[9]] * Multiplicacion)  # Esto es incorrecto, se multiplica cada elemento de la lista por 2, (Malo)

# bueno
# se debe saber el contexto siempre, no todos los ejercicios tienen que ver con programacion, pueden ser problemas matematicos o otro contexto
#solucion segun contexto matematico
Numeros[3] *= 2 #manera shorcut
Numeros[6] *= 2
Numeros[8] = Numeros[8] * 2

print(Numeros)