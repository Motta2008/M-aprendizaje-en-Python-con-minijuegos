# Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

N = int(input("Escribe un numero entero: "))
NN = N * -1
if N > 0:
    print("El valor absoluto del numero es:", N)
else:
    if N < 0:
        print("El valor absoluto del numero",  N, "es:", NN)

# format y condicional en variable en print

if numero > 0:
    print("El valor absoluto {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es:", format(numero), numero * -1)