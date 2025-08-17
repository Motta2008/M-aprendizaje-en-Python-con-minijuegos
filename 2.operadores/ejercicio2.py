# Ejercicio 2
"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.
"""
# En variable
payaso = 112
muñeca = 75
peso_total = (payaso * 23) + (muñeca * 54)

print("El peso total de la venta es de: ", peso_total, "gramos") # bueno pero poco limpio y rapido

# 

print("El peso total de los juguetes es: ", ((23*112) + (54*75)), "Gramos")


peso_total = ((23*112) + (54*75))
print("El peso total de los juguetes es: ", peso_total, "Gramos")
