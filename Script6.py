#Tarea 6#
shipping_cost_per_kg = 1.20
customer_basket_cost = 101
customer_basket_weight = 44

if(customer_basket_cost >= 100):
    print('Free shipping!')
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_basket_cost = shipping_cost
    
print("Total basket cost including shipping is " + str(customer_basket_cost))

#Con el código original el texto que se ejecuta es: Total basket cost including shipping is 52.8#
#Modificando la varible customer_basket_cost a 101 el texto que se ejecuta es: Free shipping!#