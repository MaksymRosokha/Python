import random

def print_menu(nouns, adjectives):
    victim_name = input("Enter the victim's name: ")
    victim_age = 0
    try:
        victim_age = int(input("Enter the victim's age: "))
        if victim_age < 0 or victim_age > 150:
            raise ValueError
    except ValueError:
        print("* * * You entered incorrectly * * *")
        return

    while True:
        print("---Choose what you want---")
        print("1. Add a new noun")
        print("2. Delete a noun")
        print("3. Add a new adjective")
        print("4. Delete an adjective")
        print("5. Generate a random insult")
        print("6. Exit")

        user_choose = 0

        try:
            user_choose = int(input("Your choose: "))
            if user_choose < 1 or user_choose > 6:
                raise ValueError
        except ValueError:
            print("* * * You entered incorrectly * * *")
            continue

        if user_choose == 1:
            print_nouns(nouns)
            noun = input("Enter your noun: ")
            add_noun(nouns, noun)
        elif user_choose == 2:
            try:
                print_nouns(nouns)
                user_index = int(input("Enter the number of the noun: "))
                if user_index < 1 or user_index > len(nouns):
                    raise ValueError
            except:
                print("* * * You entered incorrectly * * *")
                continue
            delete_noun(nouns, user_index)
        elif user_choose == 3:
            print_adjectives(adjectives)
            adjective = input("Enter your adjective: ")
            add_adjective(adjectives, adjective)
        elif user_choose == 4:
            try:
                print_adjectives(adjectives)
                user_index = int(input("Enter the number of the adjective: "))
                if user_index < 1 or user_index > len(adjectives):
                    raise ValueError
            except:
                print("* * * You entered incorrectly * * *")
                continue
            delete_adjective(adjectives, user_index)
        elif user_choose == 5:
            print(get_random_insult(victim_name, victim_age, nouns, adjectives))
        elif user_choose == 6:
            break


def add_noun(nouns, noun):
    nouns.append(noun)


def delete_noun(nouns, index):
    if len(nouns) > 2 and index >= 1 and index <= len(nouns):
        nouns.remove(nouns[index-1])


def print_nouns(nouns):
    if len(nouns) == 0:
        return

    i = 0
    while i < len(nouns):
        print(f"{i + 1}. {nouns[i]}")
        i += 1


def add_adjective(adjectives, adjective):
    adjectives.append(adjective)


def delete_adjective(adjectives, index):
    if len(adjectives) > 2 and index >= 1 and index <= len(adjectives):
        adjectives.remove(adjectives[index - 1])


def print_adjectives(adjectives):
    if len(adjectives) == 0:
        return

    i = 0
    while i < len(adjectives):
        print(f"{i + 1}. {adjectives[i]}")
        i += 1


def get_random_insult(name, age, nouns, adjectives):
    return (f"{name} to "
            f"{get_insult_by_age(age)}, "
            f"{random.choice(adjectives)}, "
            f"{random.choice(nouns)}")

def get_insult_by_age(age):
    if age < 10:
        return "nieopierzony"
    elif age < 18:
        return "niedojrzały"
    elif age < 30:
        return "młokosowaty"
    elif age < 50:
        return "przeciętny"
    else:
        return "zgrzybiały"

nouns = ["grzyb", "bęcwał"]
adjectives = ["żałosny", "tępy"]
print_menu(nouns, adjectives)
