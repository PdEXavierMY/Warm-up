coste_por_kilo = 1.20
def compra(valor_cesta, peso_cesta):
    if float(valor_cesta) > 100:
        print("Tu envío es gratuito")
    else:
        costetotal = float(peso_cesta) * coste_por_kilo
        print("El total del coste sumando el producto junto al envío es de " + str(costetotal) + "€")

compra(34, 44)