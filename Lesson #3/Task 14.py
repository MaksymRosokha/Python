import random


def choose_word(word_list):
    return random.choice(word_list)


def shuffle_letters(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def play_game():
    word_list = ["hello", "world", "how", "are", "you"]
    choice_word = choose_word(word_list)
    shuffled_letters = shuffle_letters(choice_word)

    while True:
        print("Guess the world")
        print("The world is: ", shuffled_letters)
        user_word = input("You guess it is: ")

        user_word.lower()

        if user_word == choice_word:
            print("You guessed")
            break
        else:
            print("You didn't guess. Try again")


play_game()
