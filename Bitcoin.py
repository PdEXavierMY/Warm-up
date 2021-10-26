def bitcoin(a, b):
    euros = float(a) * float(b)
    print("You have " +  str(euros))
    if euros < 30000:
        print("¡¡¡Tu inversión está por debajo de 30000€!!!")
    else:
        print("Tu inversión está por encima de 30000")

bitcoin(1.2, 40000)