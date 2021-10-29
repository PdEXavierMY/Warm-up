def bitcoin(nbitcoin, bitcoinvalue, euro_a_dolar):
    #nbitcoin = número de bitcoin#
    #bitcoinvalue = valor de bitcoin#
    #euro_a_dolar = valor de 1 euro en dólares#
    euros = float(nbitcoin) * float(bitcoinvalue)
    dolares = euros * float(euro_a_dolar)
    print("Tienes " + str(dolares) + "$")
    print("Tienes " +  str(euros) + "€")
    if euros < 30000:
        print("¡¡¡Tu inversión está por debajo de 30000€!!!")
    else:
        print("Tu inversión está por encima de 30000")

bitcoin(1.2, 40000, 1.17)