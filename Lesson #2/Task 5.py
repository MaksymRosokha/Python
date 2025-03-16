import sys

grade = int(input("Enter your grade from 0 to 100: "))
gradeLetter = ''
if grade >= 90 and grade <= 100:
    gradeLetter = 'A'
elif grade >= 80 and grade <= 89:
    gradeLetter = 'B'
elif grade >= 70 and grade <= 79:
    gradeLetter = 'C'
elif grade >= 60 and grade <= 69:
    gradeLetter = 'D'
elif grade >= 0 and grade <= 59:
    gradeLetter = 'E'
else:
    print("You entered your grade incorrectly")
    sys.exit()

print("Your grade is ", gradeLetter)