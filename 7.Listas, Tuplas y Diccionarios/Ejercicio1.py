# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:


print("A continuacion se le mostrara una lista con datos, ingrese dos datos los cuales seran cambiados al primer y segundo lugar de la lista")

Datos = [7, 3, 'hola', 'Motta', 3.14]

print(Datos)

dato1 = input("ingrese el dato #1: ")
dato2 = input("ingrese el dato #2: ")

Datos[0] = dato1
Datos[1] = dato2


print(Datos)
# format para repaso de 
print("Ahora a lista se ve asi: {}".format(Datos))