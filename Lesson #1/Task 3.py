num1 = float(input("Enter first number: "))
if num1 > 0:
    print("Number is positive")
else:
    print("Number isn't positive")

if num1 % 2 == 0:
    print("Number is even")
else:
    print("Number isn't even")

num2 = float(input("Enter second number: "))

if num1 == num2:
    print("The numbers are the same")
else:
    print("The numbers aren't the same")

print("Area of a square: ", num1 * num1)
print("Perimeter of a square: ", num1 * 4)

print("Opposite number: ", -1 * num1)

if num1 != 0:
    print("Inverse number: 1 /", num1 )
else:
    print("Inverse number can't be calculated")

if num1 > 0:
    print("Number is positive")
elif num1 < 0:
    print("Number is negative")
else:
    print("Number equals 0")

if num1 > num2:
    print("First number is bigger")
elif num2 > num1:
    print("Second number is bigger")
else:
    print("The numbers are equals")

if (num1 < 5) and (num1 > -5):
    print("The number is between -5 and 5")
else:
    print("The number isn't between -5 and 5")

if (num1 < 5) or (num1 > 10):
    print("The number is between (-infinity, 5) or (10, infinity)")
else:
    print("The number isn't between (-infinity, 5) or (10, infinity)")