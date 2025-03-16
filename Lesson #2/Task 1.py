price = float(input("Enter the price: "))

if price <= 100:
    price -= price * 0.1
    print("Your discount is 10% and now your price is ", price)
else:
    price -= price * 0.2
    print("Your discount is 20% and now your price is ", price)
