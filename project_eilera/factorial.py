"""

Вычисление факториала
Факториалом числа называют произведение всех натуральных чисел до него включительно. Например, факториал числа 5 равен
произведению 1 * 2 * 3 * 4 * 5 = 120.

Формула нахождения факториала:

n! = 1 * 2 * … * n,

где n – это число, а n! – факториал этого числа.

Формулу можно представить в таком виде:

n! = 1 * … * (n-2) * (n-1) * n,

т. е. каждое предыдущее число меньше на единицу, чем последующее.

С помощью цикла можно найти факториал как по первой, так и второй формуле. Для вычисления факториала с помощью рекурсии
используется вторая формула.

"""

# Вычисление факториала циклом
n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)

# Вычисление факториала с помощью цикла for:
n = int(input())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)


# Нахождение факториала рекурсией
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(fac(5))

# Функция factorial() модуля math
import math
math.factorial(4)