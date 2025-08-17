# Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
# Te llamas: <nombre>
# Tu edad es: <edad>
# Eres: <sexo>

print("ingresa tus datos por favor")

nombre = input("Ingresa tu nombre: ")

edad = int(input("Ingresa tu edad: "))

sexo = input("Ingresa tu sexo (M/F): ")


print(f"Tus datos son los siguentes: \nNombre :{nombre}, \nEdad:{edad}, \nSexo:{sexo} \n¿hay algun error en ellos?".format(nombre, edad, sexo))