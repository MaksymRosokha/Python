import math

side = float(input("Enter the side of square: "))

area = side * side
print("Area: ", area)

perimeter = 4 * side
print("Perimeter: ", perimeter)

diagonal = side * math.sqrt(2)
print("Diagonal: ", diagonal)