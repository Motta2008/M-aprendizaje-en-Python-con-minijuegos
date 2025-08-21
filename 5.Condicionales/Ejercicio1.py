# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal



letra = input("intruduce una vocal: ")

if letra.lower() == "a":
    print("es vocal")
elif letra.lower() == "e":
    print("es vocal")
elif letra.lower() == "i":
    print("es vocal")
elif letra.lower() == "o":
    print("es vocal")
elif letra.lower() == "u":
    print("es vocal")
else:
    print("No es vocal")


# con metodo de operacion
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(letra, "Es una vocal")
else:
    print(letra, "No es una vocal")

# con metodo de pertenencia con in
if letra in ["a", "e", "i", "o", "u"]:
    print(letra, "Es una vocal")
else:
    print(letra, "No es una vocal")