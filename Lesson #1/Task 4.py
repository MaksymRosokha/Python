numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

if numerator < denominator:
    print("Proper fraction")
else:
    print("Improper fraction")

    intPart = int(numerator / denominator)
    numeratorPart = numerator % denominator

    if numeratorPart == 0:
        print(f"After the change to mixed is: {intPart}")
    else:
        print(f"After the change to mixed is: {intPart} {numeratorPart}/{denominator}")