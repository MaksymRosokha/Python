import sys


def order_Tshirt(size, color, text):
    print(f"Size: {size}\nColor: {color}\nText: \"{text}\"\n")


size = ""
color = ""
text = ""

try:
    size = input("Enter size: ")
    color = input("Enter color: ")
    text = input("Enter text: ")
except ValueError:
    print("You entered incorrectly")
    sys.exit()

order_Tshirt(size, color, text)

try:
    size = input("Enter size: ")
    color = input("Enter color: ")
    text = input("Enter text: ")
except ValueError:
    print("You entered incorrectly")
    sys.exit()

order_Tshirt(size=size, color=color, text=text)