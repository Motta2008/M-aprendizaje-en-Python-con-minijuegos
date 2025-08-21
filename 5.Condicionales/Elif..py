letra = "A"

if letra.lower() == "a":
    print("Esta vocal es la A")
elif letra.lower() == "e":  #elif es una sola condicion con if
    print("Esta vocal es la E")
elif letra.lower() == "i":
    print("Esta vocal es la I")
elif letra.lower() == "o":
    print("Esta vocal es la O")
else:
    print("Esta vocal es la U") # como no se cumplen las demas condiciones no hay necesidad de colocar mas condiciones si no terminar con else la ultima y unica condicion