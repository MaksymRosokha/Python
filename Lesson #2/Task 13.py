import random

num = random.randint(1, 100)
attempts = 0

while True:
    userNum = 0

    try:
        userNum = int(input("Enter a number [1, 100]: "))
    except ValueError:
        break

    if num == userNum:
        print("You guessed!")
        break
    elif num > userNum:
        print("The number is bigger")
    else:
        print("The number is smaller")

    attempts += 1
    print("__________________________________________")

print(f"You used {attempts} attempts")