def getSquares(numbers):
    squares = []
    for num in numbers:
        squares.append(num**2)

    return squares

arr = []
for i in range(0, 10):
    arr.append(i**2)

print(arr)

numbers = [-1, 2, -6, 9]
print(getSquares(numbers))