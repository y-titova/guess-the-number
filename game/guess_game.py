import random


def binary_search_game(min_number, max_number):
    print(f"Загадай число от {min_number} до {max_number}.")
    print("Я попробую его угадать!")
    print()

    left = min_number
    right = max_number
    attempts = 0

    while left <= right:
        middle = (left + right) // 2
        attempts += 1

        print(f"Моя попытка: {middle}")

        answer = input(
            "Твоё число больше, меньше или равно? "
            "(больше/меньше/равно): "
        ).lower()

        if answer == "равно":
            print(f"Угадал! Мне понадобилось {attempts} попыток.")
            return

        if answer == "больше":
            left = middle + 1

        elif answer == "меньше":
            right = middle - 1

        else:
            print("Я не понял ответ. Попробуй ещё раз.")
            attempts -= 1

    print("Кажется, где-то была ошибка в ответах.")


binary_search_game(1, 100)