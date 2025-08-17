verdadero = True
falso = False

# Hacen referencia a condiciones entre datos, tambien pueden ser vistos como comparaciones

# ==, !=, <, >, <=, >= (Dependen del lenguaje)

# Ejemplo en booleanos
print(5 == 7)  # False
print(5 != 3)       # True
print(6 < 20)        # True
print(7000 > 1)        # True
print(7 <= 7)       # True
print( 7 >= 9)       # False

# Operadores Lógicos
#tambien pueden ser vistos como comparaciones
# and, or, not
print(verdadero and falso)  # False
print(verdadero or falso)   # True
print(not verdadero)        # False cambia el valor de lo que en verdad es el dato

# print(3.14 > 3 --> True --> False)
print(99 != 99 and 23 == 23)  # False
print(99 != 99 or 23 == 23)   # True con que una sola se cumpla en or es True
print(not (99 != 99 or 23 == 23))  # False