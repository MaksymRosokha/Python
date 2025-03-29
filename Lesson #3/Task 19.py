def print_menu(results):
    while (True):
        print("---Choose what you want---")
        print("1. Add new result")
        print("2. Delete a result")
        print("3. Sort results")
        print("4. Show results")
        print("5. Exit")

        user_choose = 0

        try:
            user_choose = int(input("Your choose: "))
            if user_choose < 1 or user_choose > 5:
                raise ValueError

        except ValueError:
            print("* * * You entered incorrectly * * *")
            continue

        if user_choose == 1:
            result = input("Enter your result: ")
            add_result(results, result)
        elif user_choose == 2:
            try:
                index = int(input("Enter the number of your result: "))
                if index < 1 or index > 5:
                    raise ValueError
            except:
                print("* * * You entered incorrectly * * *")
                continue
            delete_result(results, index)
        elif user_choose == 3:
            sort_results(results)
            show_results(results)
        elif user_choose == 4:
            show_results(results)
        elif user_choose == 5:
            break


def add_result(results, result):
    if len(results) < 5:
        results.append(result)
    else:
        results[results.index(min(results))] = result


def delete_result(results, index):
    if index <= len(results) and index > 0:
        results.remove(results[index - 1])


def sort_results(results):
    results = results.sort()


def show_results(results):
    if len(results) == 0:
        return

    i = 0
    while i < len(results):
        print(f"{i + 1}. {results[i]}")
        i += 1


print("- - - Save your top 5 results - - -")
results = []
print_menu(results)
