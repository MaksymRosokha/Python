import sys

def convertCelsiusToFahrenheit(degree):
    return 9 / 5 * degree + 32

def getUserInput():
    try:
        return int(input("Enter degrees in Celsius: "))
    except ValueError:
        print("You entered incorrectly")
        sys.exit()

userDegree = getUserInput()

while userDegree > -273.15:
    print(convertCelsiusToFahrenheit(userDegree))
    userDegree = getUserInput()