import sys


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

n = 0
try:
    n = int(input("Enter a positive number: "))
    if n < 0:
        raise ValueError
except ValueError:
    print("You entered incorrectly")
    sys.exit()

while n != 1:
    n = collatz(n)