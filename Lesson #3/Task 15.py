import random


def choose_word(word_list):
    return random.choice(word_list)

def check_letter(word, letter):
    return True if letter in word else False

def play_game():
    word_list = ["hello", "world", "how", "are", "you"]
    choice_word = choose_word(word_list)

    print("Guess the world")
    print("The world has: ", len(choice_word), " letters")
    print("You can ask for a letter 5 times")
    i = 1
    while i <= 5:
        user_letter = input(f"{i}.Your letter: ")
        user_letter.lower()

        if check_letter(choice_word, user_letter):
            print("YES")
        else:
            print("NO")

        i += 1

    print("Your attempts were finished")
    user_word = input("You think the word is: ")
    user_word.lower()

    if user_word == choice_word:
        print("You guessed")
    else:
        print("You didn't guess")

play_game()
