import sys


def getSumOfFirstSequence(maxLimit):
    sum = 0
    for i in range(2, maxLimit + 2):
        sum += 1 / i

    return sum


def getSumOfSecondSequence(maxLimit):
    sum = 0
    for i in range(2, maxLimit + 2):
        sum += (-1) ** (i - 1) / i

    return sum


maxLimit = 0

try:
    maxLimit = int(input("Enter max limit of the sequence sum (from 1): "))

    if maxLimit < 1:
        raise ValueError

except ValueError:
    print("You entered something incorrectly. Try again")
    sys.exit()

print("For 10 elements sequence's sums are:")
print(getSumOfFirstSequence(10))
print(getSumOfSecondSequence(10))
print()

print("For 100 elements sequence's sums are:")
print(getSumOfFirstSequence(100))
print(getSumOfSecondSequence(100))
print()

print("For 1000 elements sequence's sums are:")
print(getSumOfFirstSequence(1000))
print(getSumOfSecondSequence(1000))
print()

print(f"For {maxLimit} elements sequence's sums are:")
print(getSumOfFirstSequence(maxLimit))
print(getSumOfSecondSequence(maxLimit))
print()
