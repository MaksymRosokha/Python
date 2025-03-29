import random

def throw():
    return random.randint(2, 12)

def single_game():
    threwResult = throw()
    print(f"You threw {threwResult}")

    if threwResult == 7 or threwResult == 11:
        print("You won")
        return True
    elif threwResult == 2 or threwResult == 3 or threwResult == 12:
        print("You failed")
        return False

    print("You have \"Punkt\"")
    threwResult = throw()
    print(f"You threw {threwResult}")

    if threwResult == 2 or threwResult == 3 or threwResult == 7 or threwResult == 12:
        print("You failed")
        return False

    print("You won")
    return True


wonGames = 0
failedGames = 0

isPlaying = 1

while isPlaying == 1:
    try:
        isPlaying = int(input("Are we playing? (1 - yes, 0 - no): "))
    except ValueError:
        print("You entered something incorrectly. Try again")
        continue

    if isPlaying == 0:
        break
    if single_game():
        wonGames += 1
    else:
        failedGames += 1

print(f"You won {wonGames} times")
print(f"You failed {failedGames} times")