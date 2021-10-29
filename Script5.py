#Tarea 5#
dinero = 2000
precio_helado = 100
precio_helado_nuevo = precio_helado
#Se incrementa cada vez que compras uno un 20%#
porcentaje_hambre = int(input())
porcentaje_hambre_nuevo = porcentaje_hambre
if porcentaje_hambre > 85:
    print("Ya estoy satisfecho!!")
else:
    print("Tengo hambre(estoy lleno tan solo un " + str(porcentaje_hambre) + "%).")
    while porcentaje_hambre_nuevo < 100:
        porcentaje_hambre_nuevo += porcentaje_hambre
        dinero -= precio_helado_nuevo
        precio_helado_nuevo += (precio_helado * (20/100))
        if porcentaje_hambre_nuevo >= 85:
            if porcentaje_hambre_nuevo > 100:
                porcentaje_hambre_nuevo = 100
            print("Ya estoy satisfecho!!(Por fin estoy lleno al " + str(porcentaje_hambre_nuevo) + "%).")
            print("Me sobran " + str(dinero) + "€.")
            break
        else:
            print("Sigo con hambre(estoy lleno tan solo un " + str(porcentaje_hambre_nuevo) + "%).")
            if dinero <= 0:
                print("No me queda más dinero")
                break
            else:
                print("Me quedan " + str(dinero) + "€.")