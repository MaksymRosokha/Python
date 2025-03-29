word_info = dict()

user_word = input("Enter a word: ")

for i in user_word:
    if i in word_info:
        word_info[i] += 1
    else:
        word_info[i] = 1



for key in word_info:
    print(f"Letter '{key}' was {word_info[key]} times")