"""

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

"""


import time


# Пробую разные алгоритмы, чтобы проверить какой быстрее работает

# # Вариант 1 (придумал сам)
#
# # Получаем начальное время в секундах от начала времен для замера скорости работы данной реализации
# start_1 = time.time()
#
# next_number_of_fibonacci_list = 0
#
# list_of_number = list(range(1, 110)) # Мне не нравится эта реализация, так как она не изящная. Попробую сделать V2
#
# list_of_fibonacci = list()
#
# for i in list_of_number:
#     if next_number_of_fibonacci_list < 4000000:
#         if i > 2:
#             next_number_of_fibonacci_list = list_of_fibonacci[-1] + list_of_fibonacci[-2]
#             if next_number_of_fibonacci_list < 4000000: # Ограничиваю создание списка
#                 list_of_fibonacci.append(next_number_of_fibonacci_list)
#             else:
#                 break
#         else:
#             list_of_fibonacci.append(i)
#     else:
#         break
#
#
# odd_list_of_fibonacci = list()
#
# for n in list_of_fibonacci:
#     if n % 2 == 0:
#         odd_list_of_fibonacci.append(n)
#
# print(list_of_number)
# print(list_of_fibonacci)
# print(odd_list_of_fibonacci)
# print(sum(odd_list_of_fibonacci))
#
#
# # Получаем конечное время
# print(time.time() - start_1)


# Вариант 2 (подсмотрел идею более изящной реализации здесь http://pythoneuler.blogspot.com/2016/09/2.html, но буду делать сам)

# Получаем начальное время в секундах от начала времен для замера скорости работы данной реализации
start_2 = time.time()

list_of_fibonacci_2 = [0, 1]

# Считаем количество элементов в ряде Фибоначчи. Начинаем с 1,
# так как последнее число в начальном списке стоит на позиции 1
i = 0

while (list_of_fibonacci_2[-1] + list_of_fibonacci_2[-2]) < 4000000:

    list_of_fibonacci_2.append(list_of_fibonacci_2[-1] + list_of_fibonacci_2[-2])
    i += 1

# Фильтрую базовый ряд Фибоначчи через лямбду (одноразовую функцию) и достаю только парные числа. На основании их
# формирую список.
odd_list_of_fibonacci_2 = list(filter(lambda x: x % 2 == 0, list_of_fibonacci_2))


print(list_of_fibonacci_2)
print(sum(odd_list_of_fibonacci_2))

# Получаем конечное время
print(time.time() - start_2)