"""

Проверка простоты числа перебором делителей
Перебор делителей – это алгоритм, применяемый для определения, является ли натуральное число простым, или оно является
сложным, то есть составным.

Простые числа - это натуральные числа больше единицы, которые делятся нацело только на единицу и на себя. Например,
число 3 простое, так как нацело делится только на 1 и 3. Число 4 сложное, так как нацело делится не только на 1 и 4,
но также на число 2.

Алгоритм перебора делителей заключается в последовательном делении заданного натурального числа на все целые числа,
начиная с двойки и заканчивая значением меньшим или равным квадратному корню из тестируемого числа.

Если хотя бы один делитель делит исследуемое число без остатка, то это число является составным. Если ни одного такого
делителя не находится, то число признается простым.

"""

import math

n = int(input())

if n < 2:
    print("Число должно быть больше 1")
    quit()
elif n == 2:
    print("Это простое число")
    quit()

i = 2  # первый делитель

limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("Это сложное число")
        quit()  # выход из программы
    i += 1  # переход к следующему делителю

print("Это простое число")

from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(3):
    num = int(input())
    print(is_prime(num))