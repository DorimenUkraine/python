"""

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

"""

import time

# Пробую разные алгоритмы, чтобы проверить какой быстрее работает

# Вариант 1 (придумал сам)

# Получаем начальное время в секундах от начала времен
start_1 = time.time()

natural_numbers_sum = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        natural_numbers_sum += i


print(natural_numbers_sum)
# Получаем конечное время
print(time.time() - start_1)


# Вариант 2 (нашел в интернете http://pythoneuler.blogspot.com/2016/09/1.html)

# Получаем начальное время в секундах от начала времен
start_2 = time.time()

a=[x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]

print(sum(a))

# Получаем конечное время
print(time.time() - start_2)
