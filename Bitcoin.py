def bitcoin(a, b, c):
    #a = número de bitcoin#
    #b = valor de bitcoin#
    #c = valor de 1 euro en dólares#
    euros = float(a) * float(b)
    dolares = euros * float(c)
    print("Tienes " + str(dolares) + "$")
    print("Tienes " +  str(euros) + "€")
    if euros < 30000:
        print("¡¡¡Tu inversión está por debajo de 30000€!!!")
    else:
        print("Tu inversión está por encima de 30000")

bitcoin(1.2, 40000, 1.17)