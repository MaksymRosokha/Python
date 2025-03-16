import sys
import random

userNum = 0
attempts = 0
smallestNumber = 1
biggestNumber = 100

try:
    userNum = int(input("Enter a number [1, 100]: "))
except ValueError:
    sys.exit()

while True:
    compNum = random.randint(smallestNumber, biggestNumber)

    isGuessed = int(input(f"Is your number {compNum}? (1 - Yes; 0 - No): "))

    if isGuessed == 1:
        print(f"I guessed! Your number is {compNum}")
        break
    else:
        isSmaller = int(input("Is your number smaller? (1 - Yes; 0 - No):"))
        if isSmaller == 1:
            biggestNumber = compNum - 1
        else:
            smallestNumber = compNum + 1

    attempts += 1
    print("__________________________________________")

print(f"I used {attempts} attempts")