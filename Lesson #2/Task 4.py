year = int(input("Enter year: "))

isLeapYear = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False
    else:
        isLeapYear = True

if isLeapYear:
    print("The year is leap")
else:
    print("The year isn't leap")
