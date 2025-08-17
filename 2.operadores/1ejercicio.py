# libreria pow

calculo = pow ((3+2) / (2*5), 2)

print("El resultado de la operación pow es:", calculo)


#ejercicio 1
"""
Escribir un programa que realice la siguiente operación aritmética:
"""
n1 = 3
n2 = 2
n3 = 5
n4 = 2.5

Resultado = (n1 + n2 / n2 * n3) ** n2 # MALO, la jerarquia de operaciones esta mal, se debe dejar entre parentesis el denominador y el numerador

print("El resultado de la operación es:", Resultado)


#Print
print(((3+2) / (2*5))**2) # BUENO, la jerarquia de operaciones esta bien, se deja entre parentesis el denominador y el numerador
#####################################

# En una variable
calculo = ((3+2) / (2*5))**2
print("El resultado de la operación es:", calculo)


