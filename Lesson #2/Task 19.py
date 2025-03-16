def printCalendar(amountOfDays, numberOfDay):
    for i in range(1, 7 - numberOfDay + 1):
        print("   ", end=" ")
    for i in range(1, numberOfDay + 1):
        print(f" {i} ", end=" ")
    print()
    for i in range(1, amountOfDays + 1 - numberOfDay):
        if i + numberOfDay < 10:
            print(f" {i + numberOfDay} ", end=" ")
        else:
            print(f"{i + numberOfDay} ", end=" ")

        if i % 7 == 0:
            print()
    print()


while True:
    try:
        print("_____________________________________________________")
        print("If you want to stop the program, press \"Enter\"")
        amountOfDays = int(input("Enter count of days in the month: "))
        numberOfDay = int(input("Enter the day number (1-7): "))

        if amountOfDays < 28 or amountOfDays > 31 or numberOfDay < 1 or numberOfDay > 7:
            raise Exception

        printCalendar(amountOfDays, numberOfDay)
    except ValueError:
        print("Goodbye")
        break
    except Exception:
        print("You entered something incorrectly")