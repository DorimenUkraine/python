"""

Стандартная библиотека Python содержит модуль turtle, предназначенный
для обучения программированию. Этот модуль содержит набор функций,
позволяющих управлять черепахой. Черепаха умеет выполнять небольшой
набор команд, а именно:

Команда	Значение
forward(X)	Пройти вперёд X пикселей
backward(X)	Пройти назад X пикселей
left(X)	Повернуться налево на X градусов
right(X)	Повернуться направо на X градусов
penup()	Не оставлять след при движении
pendown()	Оставлять след при движении
shape(X)	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
stamp()	Нарисовать копию черепахи в текущем месте
color()	Установить цвет
begin_fill()	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
end_fill()	Вызвать после окончания рисования фигуры
width()	Установить толщину линии
goto(x, y)	Переместить черепашку в точку (x, y)

http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#while

"""

import turtle
import math

# step = 0
# square_side = 2
# growth_side = 1

# Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный многоугольник с большим числом сторон будет
# выглядеть как окружность. Пример:
# while step <= 40:
#     turtle.shape('turtle')
#     turtle.left(9)
#     turtle.forward(10)
#     step += 1

# Нарисуйте «квадратную» спираль.
# while step <= 50:
#     turtle.shape('turtle')
#     turtle.forward(square_side/2)
#     turtle.left(90)
#     turtle.forward(square_side)
#     step += 1
#     square_side += growth_side

# Нарисуйте спираль. См. теорию Архимедова спираль в Википедии
# while step <= 500:
#     turtle.shape('turtle')
#     turtle.forward(square_side/10)
#     turtle.left(10)
#     step += 1
#     square_side += growth_side

"""

Нарисуйте 10 вложенных правильных многоугольников. Используйте функцию, рисующую правильный n-угольник. Формулы для нахождения
радиуса описанной окружности (Радиус описанной окружности правильного многоугольника, формула). Пример:

"""

# turtle.shape('turtle')
# n = 3
# r = 10  # задаем радиус первой окружности
#
#
# def more_agles(n, m):  # определяем функцию, рисующую многоугольник
#     q = 360 / n
#     while n > 0:
#         turtle.left(q)
#         turtle.forward(m)
#         n -= 1
#
#
# while n < 13:
#     m = 2 * r * math.sin(math.pi / n)  # считаем размер стороны многоугольника (a=2Rsin (360/2n))
#     x = (180 - 360 / n) / 2
#     turtle.left(x)
#
#     more_agles(n, m)
#     turtle.right(x)
#     turtle.penup()
#     turtle.forward(10)  # задаем расстояние м/у окружностями
#
#     turtle.pendown()
#     n += 1
#     r += 10  # раз расстояние м/у окружностями 10, увеличиваем радиус на 10

"""

Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность

"""


def main():
    circle(0, 0, 1)
    circle(0, 0, 2)
    circle(0, 60, 1)
    circle(0, 0, 2)
    circle(0, 60, 1)
    circle(0, 0, 2)


def circle(step, angle, number_of_circle):
    turtle.left(angle)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    while step <= 40:
        turtle.shape('turtle')
        if number_of_circle == 1:
            turtle.left(9)
        elif number_of_circle == 2:
            turtle.right(9)
        turtle.forward(10)
        step += 1


main()