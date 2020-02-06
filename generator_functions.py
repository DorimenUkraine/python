# # Generators - это iterators
# # Не каждый итератор - генератор
#
# # def my_funtion(x):
# #     return x
# #
# # print(my_funtion(4))
#
#
# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
#
# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
#
# counter = count_up_to(10)
#
# # for number in counter:
# #     print(number)
#
# counter.__next__()
#


"""

Создайте функцию-генератор get_week_day(),
которая создаёт генератор, вырабатывающий один день
недели за раз, Дни недели должны начинаться с
воскресенья и заканчиваться субботой.

"""


# def get_week_day():
#     week = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]
#     for day in week:
#         yield day


def even_odd():
    value = 'even'
    while True:
        yield value
        if value == 'even':
            value = "odd"
        else:
            value = "even"
            

print(even_odd())