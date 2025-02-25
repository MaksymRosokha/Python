import math

h = 1
a = float(input("Enter diagonal for pyramid: "))

areaOfBase = a * math.sqrt(2)
sideOfBase = math.sqrt(a/2)
triangleArea = (sideOfBase*h)/2

volume = 1/3 * areaOfBase * h
fullArea = areaOfBase + 4 * triangleArea

print(f"Full area of pyramid: {fullArea}")
print(f"Volume of pyramid: {volume}")