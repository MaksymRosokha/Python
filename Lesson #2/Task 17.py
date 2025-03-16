import random

headsAmount = 0
tailsAmount = 0

for i in range(100):
    if random.randint(0,1) == 1:
        headsAmount += 1
    else:
        tailsAmount += 1

print("Heads amount is: ", headsAmount)
print("Tails amount is: ", tailsAmount)