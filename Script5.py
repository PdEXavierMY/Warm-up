#Tarea 5#
dinero = 2000
precio_helado = 100
#Se incrementa cada vez que compras uno un 20%#
porcentaje_hambre = 17
print("Tengo hambre(estoy lleno tan solo un 17%).")
while porcentaje_hambre < 100:
        porcentaje_hambre += 17
        dinero -= precio_helado
        precio_helado += (precio_helado * (20/100))
        if porcentaje_hambre >= 85:
            print("Ya estoy satisfecho!!(Por fin estoy lleno al " + str(porcentaje_hambre) + "%).")
            print("Me sobran " + str(dinero) + "€.")
            break
        else:
            print("Sigo con hambre(estoy lleno tan solo un " + str(porcentaje_hambre) + "%).")
            print("Me quedan " + str(dinero) + "€.")