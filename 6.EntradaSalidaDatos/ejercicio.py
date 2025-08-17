#Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
#3x^2-5x+2=0 x=1 x=2/3
"""

# !!!!! Mí respuesta (esta mal)

# print('a continuacion adignaras un dato a cada valor de la ecuacion')

# a = int(input('Ingresa un valor para a: '))
# b = int(input('Ingresa otro valor para b: '))
# c = int(input('Ingresa un valor para c: '))

# solucion = (-b + ((b**2) - (4*a*c))** 0.5) / (2*a)

# print('el resultado es =', solucion)


#elevar un número a la potencia de 0.5 es equivalente a calcular su raíz cuadrada.
"""

# Solucion con libreria (Correcta)

from math import sqrt # sqrt para raiz

A = int(input('Ingresa un valor para A: '))
B = int(input('Ingresa un valor para B: '))
C = int(input('Ingresa un valor para C: '))

x1 = 0
x2 = 0

if ((B**2)-(4*A*C)) < 0:
    print(" No se puede realizar  por que no se puede sacar raiz a un numero negativo")
else:
    x1 = (-B +sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("La solucion es: \nx1=",x1, "\nx2=",x2 )

# a un numero negativo no se le puede sacar raiz

# No hice el ejercicio bien y copie la solcuion del curso