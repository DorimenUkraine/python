# # Special (magic) methods __method_name__
#
#
# class Person:
#     def __init__(self, firstname, lastname, age, is_married):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.is_married = is_married
#
#     def __str__(self):
#         return self.firstname + ' ' + self.lastname
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __del__(self):
#         print('Person object with name ' + self.lastname + ' is deleted from memory')
#
#
# jack = Person('Jack', 'White', 45, True)
# jane = Person('Jane', 'Air', 23, False)
# print(jack + jane) # Определение метода add переопределяет поведение оператора сложения
#
# # print([1, 2, 3, 4, 5])
# print(jack)
# print(len(jack))
# # del (jack)
# # # print(jack)
# #
# # x = 5
# # y = 3
# #
# # a = '5'
# # b = '3'
# # print(x.__add__(y)) # Тоже самое, что x + y. тип данных не изменяется.
# # print(a.__add__(b)) # Тоже самое, что a + b. тип данных не изменяется.
# #


class Chain():
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return 'Chain with ' + str(self.number_of_items)

    def __len__(self):
        return self.number_of_items


item = Chain(10)
print(item)
print(len(item))