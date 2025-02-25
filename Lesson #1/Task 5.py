x = float(input("Enter x: "))
y = float(input("Enter y: "))

if (x > 0) and (y > 0):
    print("The point is located in the upper right quadrant")
if (x < 0) and (y > 0):
    print("The point is located in the upper left quadrant")
if (x > 0) and (y < 0):
    print("The point is located in the lower right quadrant")
if (x < 0) and (y < 0):
    print("The point is located in the lower left quadrant")
if (x == 0) or (y == 0):
    print("The point lies on the axis")