n = 0

while True:
    try:
        print("____________________________________________")
        n = int(input("Enter n (n > 1): "))
        print("____________________________________________")

        if n <= 1:
            raise ValueError

        break
    except ValueError:
        print("You entered the n incorrectly. Try again")

print("a)")
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("b)")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
for i in range(n, 0, -1):
    print(i, end=" ")
print()

print("c)")
i = 1
while i < n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()
for i in range(1, n):
    if i % 2 == 0:
        print(i, end=" ")
print()

print("d)")
i = n
while i >= 1:
    if i % 2 != 0:
        print(i, end=" ")
    i -= 1
print()
for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i, end=" ")
print()

print("e)")
i = 1
while i <= n:
    print(i, end=" ")
    i += 3
print()
for i in range(1, n + 1, 3):
    print(i, end=" ")
print()

print("f)")
i = 1
while i <= 12:
    j = 1
    factor = 1
    while j <= i:
        factor *= j
        j += 1
    print(factor, end=" ")
    i += 1
print()
for i in range(1, 13):
    factor = 1
    for j in range(1, i + 1):
        factor *= j
    print(factor, end=" ")
print()

print("g)")
i = 1
while i <= n:
    print("{:.3f}".format(1 / i), end=" ")
    i += 1
print()
for i in range(1, n + 1):
    print("{:.3f}".format(1 / i), end=" ")
print()

print("h)")
i = 2
a = 3
print(a, end=" ")
while i <= 17:
    a = 6 * a - 13 / 2
    print("{:.3f}".format(a), end=" ")
    i += 1
print()
a = 3
print(a, end=" ")
for i in range(2, 18):
    a = 6 * a - 13 / 2
    print("{:.3f}".format(a), end=" ")
print()

print("i)")
i = 1
a = 0
print(a, end=" ")
while i <= 31:
    a = 2 * a + 1
    print(a, end=" ")
    i += 1
print()
a = 0
print(a, end=" ")
for i in range(0, 31):
    a = 2 * a + 1
    print(a, end=" ")
print()

print("j)")
i = 1
sum = 0
while i <= n:
    sum += i ** 2
    i += 1
print(sum)
sum = 0
for i in range(1, n + 1):
    sum += i ** 2
print(sum)

print("k)")
i = 1
sum = 0
while i <= n:
    sum += i * 2
    i += 1
print(sum)
sum = 0
for i in range(1, n + 1):
    sum += i * 2
print(sum)

print("l)")
i = 1
sum = 1
while i < n:
    sum += i * 2 + 1
    i += 1
print(sum)
sum = 1
for i in range(1, n):
    sum += i * 2 + 1
print(sum)

print("m)")
i = 1
even = 0
odd = 0
while i <= n:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1
print(f"Even amount is {even} and odd amount is {odd}")
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even amount is {even} and odd amount is {odd}")

print("n)")
i = 1
positive = 0
negative = 0
while i <= n:
    if i > 0:
        positive += 1
    else:
        negative += 1
    i += 1
print(f"Positive amount is {positive} and negative amount is {negative}")
positive = 0
negative = 0
for i in range(1, n + 1):
    if i > 0:
        positive += 1
    else:
        negative += 1
print(f"Positive amount is {positive} and negative amount is {negative}")

print("o)")
i = 1
divisibleByThree = 0
while i <= n:
    if i % 3 == 0:
        divisibleByThree += 1
    i += 1
print(divisibleByThree)
divisibleByThree = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        divisibleByThree += 1
print(divisibleByThree)

print("p)")
i = 1
divisibleByFive = 0
while i <= n:
    if i % 5 == 0:
        divisibleByFive += 1
    i += 1
print(divisibleByFive)
divisibleByFive = 0
for i in range(1, n + 1):
    if i % 5 == 0:
        divisibleByFive += 1
print(divisibleByFive)

print("q)")
i = 1
sum = 0
while i <= n:
    sum += 1 / i
    i += 1
print(sum)
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print(sum)

print("r)")
i = 1
sum = 0
while i <= n:
    sum += 1 / (i ** 2)
    i += 1
print(sum)
sum = 0
for i in range(1, n + 1):
    sum += 1 / (i ** 2)
print(sum)
