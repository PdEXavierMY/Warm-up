#Tarea 8#
investment_in_bitcoin = 1.2
bitcoin_to_euros = 40000

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euro_value = bitcoin_amount * bitcoin_value_euros
    return euro_value
investment_in_euro = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)
if investment_in_euro <= 30000:
    print("Investment below 30,000€! SELL!")
else:
    print("Investment above 30,000€")


investment_in_bitcoin2 = 1.2
bitcoin_to_euros2 = 25000

def bitcoinToEuros2(bitcoin_amount2, bitcoin_value_euros2):
    euro_value2 = bitcoin_amount2 * bitcoin_value_euros2
    return euro_value2
investment_in_euro2 = bitcoinToEuros2(investment_in_bitcoin2, bitcoin_to_euros2)
if investment_in_euro2 <= 30000:
    print("Investment below 30,000€! SELL!")
else:
    print("Investment above 30,000€")