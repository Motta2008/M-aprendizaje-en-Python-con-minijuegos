#Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

Meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = (int(input("ingrese un numero del 1 al 12 para mostrar un mes: ")))

print(Meses[numero - 1])
# se resta uno al indice para que se alinee con la tupla que empieza en 0 y encaje el numero con el mes correspondiente o tambien numero -= 1