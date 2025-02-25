day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if (day >= 1) and (day <= 31):
    if (month >= 1) and (month <= 12):
        if (year >= 1900) and (year <= 2050):
            if day < 10:
                day = '0' + str(day)
            if month < 10:
                month = '0' + str(month)

            print(f"{day}.{month}.{year}")