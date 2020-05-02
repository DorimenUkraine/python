"""

Числа Фибоначчи: циклом и рекурсией
Числа Фибоначчи – это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, ...
. Иногда ряд начинают с нуля: 0, 1, 1, 2, 3, 5, ... . В данном случае мы будем придерживаться первого варианта.

Формула:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2

Пример вычисления:

F3 = F2 + F1 = 1 + 1 = 2
F4 = F3 + F2 = 2 + 1 = 3
F5 = F4 + F3 = 3 + 2 = 5
F6 = F5 + F4 = 5 + 3 = 8

"""

# Вычисление n-го числа ряда Фибоначчи с помощью цикла while
fib1 = 1
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)

# Компактный вариант кода:
fib1 = fib2 = 1

n = int(input("Номер элемента ряда Фибоначчи: ")) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print(fib2)

# Вывод чисел Фибоначчи циклом for
fib1 = fib2 = 1

n = int(input())

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print()

# Рекурсивное вычисление n-го числа ряда Фибоначчи
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))