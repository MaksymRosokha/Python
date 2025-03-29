def print_without_vowels(text):
    for i in text:
        if not is_vowel(i):
            print(i, end="")
    print()

def is_vowel(letter):
    for j in ['a', 'e', 'o', 'i', 'u']:
        if letter == j:
            return True
    return False

text = input("Enter some text:\n")
print_without_vowels(text)