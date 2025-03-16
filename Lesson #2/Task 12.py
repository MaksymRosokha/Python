def isPrime(num):
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True


while True:
    try:
        num = int(input("Enter a number > 1: "))
    except ValueError:
        break

    if isPrime(num):
        print("The number is prime\n")
    else:
        print("The number isn't prime\n")