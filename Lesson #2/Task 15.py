rows = 0

while True:
    try:
        rows = int(input("Enter amount of rows: "))
        if rows < 1:
            raise Exception

        break
    except Exception:
        print("You entered the amount of rows incorrectly")
        print("Try again...")

stars = 1
spaces = rows

for i in range(0, rows):
    for j in range(0, spaces - 1):
        print(" ", end= ' ')

    for j in range(0, stars):
        print("*", end= ' ')

    print()
    stars += 2
    spaces -= 1