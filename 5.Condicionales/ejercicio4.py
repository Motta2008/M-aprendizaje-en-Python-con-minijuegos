# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

print("A continuacion votara por alguno de los siguientes candidatos y se le dira el color del partido por el cual voto")
candidato = input("Ingrese el candidato a votar por favor \nA \nB \nC \n-")

if candidato.upper() == "A":
    print("El color del partido es Rojo")
elif candidato.upper() == "B":
    print("El color del partido es Verde")
elif candidato.upper() == "C":
    print("El color del partido es Azul")
else:
    print("El candidato no es valido")