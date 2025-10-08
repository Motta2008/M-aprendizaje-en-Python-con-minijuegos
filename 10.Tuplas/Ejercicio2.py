# Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

Alfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

Numero = int(input("Ingrese un numero para mostrar la letra del alfabeto correspondiente: "))

print(Alfabeto[Numero - 1])