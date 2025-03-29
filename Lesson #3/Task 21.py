import random


def print_hangings(mistakes_amount):
    if mistakes_amount == 1:
        print("""
          _______
          |/
          |
          |
          |
          |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 2:
        print("""
          _______
          |/
          |     ( )
          |
          |
          |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 3:
        print("""
          _______
          |/
          |     ( )
          |      |
          |
          |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 4:
        print("""
          _______
          |/
          |     ( )
          |      |_
          |        \\
          |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 5:
        print("""
          _______
          |/
          |     ( )
          |     _|_
          |    /   \\
          |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 6:
        print("""
          _______
          |/
          |     ( )
          |     _|_
          |    / | \\
          |      |
          |
          |
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 7:
        print("""
          _______
          |/
          |     ( )
          |     _|_
          |    / | \\
          |      |
          |     / \\
          |    /   \\
          |
        __|________
        |         |
        """)
    elif mistakes_amount == 8:
        print("""
          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     / \\
          |    /   \\
          |
        __|________
        |         |

     * * *  RIP  * * *
        """)

def play(word):
    hid_word = '_' * len(word)
    failed_attempts = 0

    while (not hid_word == word) and (failed_attempts <= 8):
        print(hid_word)
        letter = ''
        try:
            letter = input("Enter a letter: ")
        except ValueError:
            print("You entered incorrectly")
            continue

        new_hid_word = get_new_hid_word(word, letter, hid_word)

        if new_hid_word == hid_word:
            failed_attempts += 1
            print_hangings(failed_attempts)
        else:
            hid_word = new_hid_word

    if hid_word == word:
        print("Greetings")
        print(f"You guessed the word: {hid_word}")

def get_new_hid_word(word, letter, hid_word):
    hid_word = list(hid_word)
    for i in range(len(word)):
        if word[i] == letter:
            hid_word[i] = letter

    return "".join(hid_word)



words = ['elephant', 'lemon', 'notebook', 'lemon', 'lemon', 'mountain', 'lemon',
         'elephant', 'kite', 'cherry', 'dog', 'apple', 'cherry', 'house', 'forest',
         'cherry', 'notebook', 'elephant', 'guitar', 'sun']

play(random.choice(words))
