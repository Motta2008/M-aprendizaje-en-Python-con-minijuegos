# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
# se coloca float ya que las notas son de decimales y no necesariamente enteras
P1 = float(input('ingresa la nota de tu primera practica: '))
P2 = float(input('Ingresa la nota de tu segunda practica: '))
P3 = float(input('Ingresa la nota de tu tercera practica: '))

EP = float(input('Ingrese la nota del examen parcial: '))
EF = float(input('Ingrese la nota del examen final: '))

PROMPRACT = ( P1 + P2 + P3) / 3
PROMFIN = (PROMPRACT + 2*EP + 3*EF) / 6

print('Su promedio e practica es:\n ', PROMPRACT, "\n Y su promedio final es:\n ", PROMFIN)