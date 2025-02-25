import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = math.pow(b,2) - (4 * a * c)

if d < 0:
    print("No roots")
elif d == 0:
    x = -b / (2 * a)
    print(f"For a={a}, b={b}, c={c}")
    print(f"x={x}")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    print(f"For a={a}, b={b}, c={c}")
    print(f"x1={x1}, x2={x2}")
