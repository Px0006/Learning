def calcTax(price, tax_rate):
    taxTotal = price +(price*tax_rate)
    return taxTotal

my_price = float(input("Enter a price: "))

totalPrice = calcTax(my_price, 0.06)
print("price =", my_price, "total price:", totalPrice)
