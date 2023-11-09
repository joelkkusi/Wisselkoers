name = input("What's your name: ")

amountInput = input(name + " how many euro\'s do you want to exchange: ")

euroToDollar = 1.17
euroToPond = 0.91
euroToYen = 161.75

exchangeDollar = float(amountInput) * float(euroToDollar)
exchangePond = float(amountInput) * float(euroToPond)
exchangeYen = float(amountInput) * float(euroToYen)

messageDollar = "For " + amountInput + " euro\'s, you get " + str(exchangeDollar) + " dollar."
messagePond = "For " + amountInput + " euro\'s, you get " + str(exchangePond) + " pond."
messageYen = "For " + amountInput + " euro\'s, you get " + str(exchangeYen) + " yen."

print(messageDollar)
print(messagePond)
print(messageYen)
