"""

Python предоставляет программисту большой набор инструментов, один из которых — yield.

Он заменяет обычный возврат значений из функции и позволяет сэкономить память при обработке большого объема данных.

yield – один из тех инструментов, использовать которые вовсе не обязательно. Всё, что можно реализовать с его помощью,

можно сделать, используя обычный возврат return. Однако этот оператор позволяет не только сэкономить память,
но и реализовать взаимодействие между несколькими последовательностями в пределах одного цикла.

Что такое yield и как это работает
Yield – ключевое слово, которое используется вместо return. С его помощью функция возвращает значение без уничтожения
локальных переменных, кроме того, при каждом последующем вызове функция начинает своё выполнение с оператора yield.

Функция, содержащая yield в Python 3, называется генератором. Чтобы разобраться, как работает yield и зачем его
используют, необходимо узнать, что такое генераторы, итераторы и итерации.

Но перед этим рассмотрим пример:

"""


def numbers_range(n):
    for i in range(n):
        yield i


a = numbers_range(4)

print(type(a))
for b in a:
    print(b)



"""
Тип полученного значения при вызове функции – это генератор. Один из способов получения значений из генератора –
это их перебрать в цикле for. Им мы и воспользовались.

Но можно его легко привести к списку, как мы сделали в статье про числа Фибоначчи.

Теперь разберемся, как это всё работает.

Введение
Расчет ряда чисел Фибонначчи – один из лучших примеров программ на Python, использующих рекурсию.

Хотя наиболее частый пример, рекурсии – это расчет факториала.

Цикл
Будем искать с помощью цикла for. В переменных prew и cur будут предыдущий элемент последовательности и текущий,
их проинициализируем в 1. Если пользователь запросит первый или второй элемент, то мы так и не попадём внутрь тела цикла.
И будет выведена единица из переменной cur.

Если же запросят 3-ий или какой либо последующий элемент последовательности Фибоначчи, то мы зайдем в цикл.
Во временную переменную tmp сохраним следующее число последовательности. После этого заполним prew и cur новыми значениям.
Когда пройдет нужное количество итераций, выведем значение cur в консоль.

"""

prew = cur = 1

element = input('Введите номер искомого элемента : ')
element = int(element)

for n in range(int(element-2)):
    tmp = prew + cur
    prew = cur
    cur = tmp

print(str(element)+' элемент последовательности равен ' + str(cur))

"""
В предыдущем коде нам пришлось воспользоваться переменной tmp. Но можно код внутри цикла переписать следующим образом:
prew, cur = cur, prew + cur

Теперь вместо трех строк кода получилась одна строка! И пропала необходимость использования дополнительной переменной.

"""


prew = cur = 1

element = input('Введите номер искомого элемента : ')
element = int(element)

for n in range(int(element-2)):
    prew, cur = cur, prew + cur


"""
В этом примере мы использовали цикл for, но можно эту программу реализовать, немного изменив код, с помощью цикла while.

Генератор списка

Если мы захотим инициализировать список рядом Фибоначчи, то это можно сделать следующим образом:
"""


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = list(fibonacci(10))
print(data)

"""
Здесь fibonacci(10) это генератор объекта ряда размерностью 10. При каждом последующем вызове он будет с помощью yield
возвращать очередной элемент. Мы создаём из него список. Затем выводим список в консоль с помощью функции print.

Если нам надо будет поочередно получать числа ряда, а не держать в памяти сразу весь список, то можно поступить следующим
образом:

"""

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for i in range(5):
    print(next(gen))

"""
Здесь мы создали с помощью Python 3 генератор чисел Фибоначчи. При помощи функции next мы получаем поочередно числа ряда.

"""

"""

Что такое генераторы

Генератор — это обычная функция, которая при каждом своём вызове возвращает объект.
При этом в функции-генераторе вызывается next.

Отличие генераторов от обычной функции состоит в том, что функция возвращает только одно значение с помощью ключевого
слова return, а генератор возвращает новый объект при каждом вызове с помощью yield.
По сути генератор ведет себя как итератор, что позволяет использовать его в цикле for.

Программист может не использовать генераторы, однако в некоторых ситуациях оптимизировать программу можно только с их помощью.

"""

"""
Функция next()

Эта функция позволяет извлекать следующий объект из итератора. То есть чтобы цикл перешел с текущей итерации на следующую,
вызывается функция next(). Когда в итераторе заканчиваются элементы, возвращается значение, заданное по умолчанию,
или возбуждается исключение StopItered.

На самом деле каждый объект имеет встроенный метод __next__, который и обеспечивает обход элементов в цикле, а функция
next() просто вызывает его.

Функция имеет простой синтаксис: next(итератор[,значение по умолчанию]). Она автоматически вызывается интерпретатором
Python в циклах while и for.

Вот пример использования next:

"""

def numbers_range(n):
    for i in range(n):
        yield i
a = numbers_range(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


"""
Преимущества использования yield

yield используют не потому, что это определено синтаксисом Python, ведь всё, что можно реализовать с его помощью,
можно реализовать и с помощью обычного return.

Программисты предпочитают применять генераторы в тех случаях, когда нет необходимости сохранять всю последовательность 
и промежуточные значения в памяти.
Функция, которая обрабатывает большую последовательность и использует обычный return, требует от интерпретатора
выделять ей много памяти. И если обычно такие функции не сильно влияют на производительность программы, то в проектах,
содержащих последовательности с миллионами элементов, они потребляют очень много памяти.

Использование yield в языке программирования Python 3 позволяет не сохранять в память всю последовательность, а просто
генерирует объект при каждом вызове функции. Это позволяет обойтись без использования большого количества оперативной памяти

"""

"""
yield from

Многие считают, что yield from был добавлен в язык Python 3, чтобы объединить две конструкции: yield и цикл for,
потому что они часто используются совместно, как в следующем примере:

"""

# Обычный yield
def numbers_range(n):
    for i in range(n):
        yield i
#yield from
def numbers_range(n):
    yield from range(n)

"""
Однако истинное предназначение нововведения немного в другом. Конструкция позволяет «вкладывать» один генератор в другой,
то есть создавать субгенераторы.

yield from позволяет программисту легко управлять сразу несколькими генераторами, настраивать их взаимодействие и,
конечно, заменить более длинную конструкцию for+yield, например:

"""

def subgenerator():
    yield 'World'
def generator():
    yield 'Hello'
    yield from subgenerator() #Запрашиваем значение из субгенератора
    yield '!'
for i in generator():
    print(i, end = ' ')