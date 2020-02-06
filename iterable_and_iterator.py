# # Iterate - объект, элементы которого можно перебирать
#
# number_list = [1, 2, 3, 4, 5]
#
# for number in number_list:
#     print(number)
#
#
# for letter in 'my_string':
#     print(letter)
#
#
# # Iterators - переборщик
#
# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_list_iterator = iter('my_string')
# print(type(string_list_iterator))
#
#
# # print(string_list_iterator.__next__())
# # print(string_list_iterator.__next__())
# # print(string_list_iterator.__next__())
# # print(string_list_iterator.__next__())
# # print(string_list_iterator.__next__())
#
# # print(next(string_list_iterator))
# # print(next(string_list_iterator))
# # print(next(string_list_iterator))
# # print(next(string_list_iterator))
#
# def my_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             print('Iteration is finished')
#             break
#
# my_for_loop('hello')
# my_for_loop([1, 2, 3])

# current_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thuesday', 'Friday', 'Saturday']
# current_list_iterator = iter(current_day)
#
# print(current_list_iterator.__next__())


def get_week_day(day):
    iterator = iter(day)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break


get_week_day(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thuesday', 'Friday', 'Saturday'])