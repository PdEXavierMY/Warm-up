#Tarea 1#
print("Roses are #ff0000 Violets are #0000ff why my code´s working I haven´t a clue")

#Tarea 2#
print("Hello world")

#Tarea 3#
print(21 + 43)
print(142 - 52)
print(10 * 342)
print(5 ** 2)

#Tarea 4#
altura = 200
altura += 50
print(altura)

#Tarea 5#
dinero = 2000
precio_helado = 100
#Se incrementa cada vez que compras uno un 20%#
porcentaje_hambre = 17
print("Tengo hambre(estoy lleno tan solo un 17%).")
while porcentaje_hambre < 100:
    if porcentaje_hambre > 85:
        print("Ya estoy satisfecho!!(Por fin estoy lleno al " + str(porcentaje_hambre) + "%).")
        break
    else:
        porcentaje_hambre += 17
        precio_helado += (precio_helado * (20/100))
        print("Sigo con hambre(estoy lleno tan solo un " + str(porcentaje_hambre) + "%).")