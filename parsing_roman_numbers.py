"""

Домашнее задание: парсинг римских чисел

Написать функцию, которая принимает на вход строку - римское число, а возвращает это число в арабском виде. Например,
если передаём "XV" - должна вернуть 15, если передаём "IV" - должна вернуть 4.

Вот список римских символов и их отображение на арабские числа:

I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

Варианты типа IIIV = 5-3 = 2 мы не рассматриваем. Хотя Римляне и пользовались иногда такими видами записей, но есть
разная информация о приемлимости оных. В нашем ДЗ такие варианты мы не рассматриваем. Вот выдержка из wiki:

"Необходимо отметить, что другие способы «вычитания» недопустимы; так, число 99 должно быть записано как XCIX, но не как IC."

Подсказка. Для решения надо реализовать два правила:

Правила записи чисел римскими цифрами:

- если большая цифра стоит перед меньшей, то они складываются (принцип сложения),
- если меньшая цифра стоит перед большей, то меньшая вычитается из большей (принцип вычитания).

Защиту от некорректного ввода реализовать по вашему желанию (можно не делать, но для тренировки всегда полезно).

"""

romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1 < len(roman) and romans[roman[i]] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result


roman = input('Введите римское число: ').upper()

print(parse_roman(roman))

