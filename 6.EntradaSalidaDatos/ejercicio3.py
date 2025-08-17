#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal = input("Digita una vocal en minuscula: ")
letra = input("Digita una letra en mayuscula: ")

# print("ahora tu vocal es mayuscula", vocal.upper() + " y tu letra es minuscula " + letra.lower())

#solucion correcta
#cambiar el valor del dato desde fuera del print primero

vocal = vocal.upper()
letra = letra.lower()
print("la vocal ahora {} es MAYUSCULA   \ny la letra {} es minuscula ".format(vocal, letra))
