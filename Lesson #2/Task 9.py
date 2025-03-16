num = int(input("Enter a positive number: "))
sum = 0
i = 1

while num <= 0:
    num = int(input("Enter a positive number: "))

while i <= num:
    sum += i ** 2
    i += 1
print(sum)