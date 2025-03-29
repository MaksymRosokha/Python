def returnArithmeticMeanOfThree(a, b, c, d):
    return (a + b + c + d - min(a, b, c, d)) / 3

print(returnArithmeticMeanOfThree(1, 2, 3, 4))
print(returnArithmeticMeanOfThree(10, 20, 30, 5))
print(returnArithmeticMeanOfThree(-1, -2, -3, -4))
print(returnArithmeticMeanOfThree(7, 7, 7, 2))
