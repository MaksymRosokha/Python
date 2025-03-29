def is_palindrome(text):
    return text[::1] == text[::-1]

text = input("Enter some text:\n")

if is_palindrome(text):
    print("Entered text is palindrome")
else:
    print("Entered text isn't palindrome")