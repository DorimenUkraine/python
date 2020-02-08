"""

Реализуйте одну классическую и достаточно простую игру:
 "угадай число".

Компьютер загадывает число от 1 до 50
и даёт 6 попыток пользователю,
чтобы тот смог угадать загаданное число.

Когда пользователь вводит число, компьютер
проверяет угадано ли число и если не угадано,
то сообщает пользователю меньше ли или больше
загаданое число.

Если пользователь угадал - то сообщает о том,
что число отгадано.

Подсказка: для "загадывания" числа используйте
модуль random: импортируйте его и для генерации
(загадывания) числа вызовите метод
random.randint(1, 50).

"""

import random

# Генерируем случайное число от 1 до 50
guess_the_number = random.randint(1,50)

# Всего попыток будет 6. Установим базовое состояние - 0
number_of_attempts = 0

while number_of_attempts <= 6:
    # Просим пользователя ввести число (любое, но желательно, чтобы от 1 до 50
    input_number = int(input("Введите число от 1 до 50 "))
    if 1 <= input_number <= 50:
        # если введенное число равно сгенерированному, тогда успех
        if input_number == guess_the_number:
            print(f'Great! You are right! You input number {input_number} and our number is {guess_the_number}')
            print(f'Number of attempts: {number_of_attempts}')
            break
        # если введенное число не равно сгенерированному, тогда прибавляем к кол-ву попыток
        # и просим заново ввести число
        else:
            print(f'Sorry! You input number {input_number} and is\'n right!')
            number_of_attempts += 1
            print(f'Number of attempts: {number_of_attempts}')
            # Надо вывести пользователю, что достигли предела попыток
            if number_of_attempts == 7:
                print('Вы достигли предела попыток')
                break
            else:
                continue
    else:
        print(f'Sorry! Your number {input_number} is out of range and is\'n right!')
        number_of_attempts += 1
        print(f'Number of attempts: {number_of_attempts}')
        # Надо вывести пользователю, что достигли предела попыток
        if number_of_attempts == 7:
            print('Вы достигли предела попыток')
            break
        else:
            continue



