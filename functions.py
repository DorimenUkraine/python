# # def sum(x: "int,>0", y: int):  # "int.>0 - прошу от разработчиков, чтобы ввели числа и x был больше 0
# #     """складывает
# #     x и y"""
# #     return x + y
# #
# #
# # print(sum(1, sum(2, 3.5)))  # сначала возьмет 2 и 3.5, просуммирует их
#
#
# # потом вернется снова к печати, возьмет 1 и 5, проссумирует их и выведет 6
#
#
# # def p3(z):
# #     print(z)
# #     print(z)
# #     return  # вызовет как return None
# #     print(z)
# #
# #
# # z = p3('Hello')
# #
# # print(type(z))
#
#
# # def mult_two(a: int, b: int) -> int:
# #     return a * b
# #
# # """ Что такое if __name__ == '__main__' (if name main в языке Python)
# Конструкци if __name__ == '__main__': main()
# в Python определяет какая функция будет
# исполняться в качестве основной.
# Обычно это main().
# https://server-gu.ru/if-name-main-python/# """
# # if __name__ == '__main__':
# #     print("Example:")
# #     print(mult_two(1, 0))
# #
# #     # These "asserts" are used for self-checking and not for an auto-testing
# #     assert mult_two(3, 2) == 6
# #     assert mult_two(1, 0) == 0
# #     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# # built-in functions
# x = print('Hello!')
# y = set()
#
# print(type(x))
# print(type(y))
#
# print(x)
# print(y)
#
# # built-in methods
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     """
#     Печатает Hello
#     :return: None
#     """
#     print('Hello')
#
# # Вызов функции print_greeting для печати Hello
# print_greeting()
#
# # help (название функции) - выводит описание к функции
# help(print_greeting)


# def print_greeting_with_name(name = "Name"): # "Name" - значение по-умолчанию, если при вызове функции пусто
#     """
#     :param name
#     :return: None
#     """
#     print("Hello " + name + "!")
#
#
# print_greeting_with_name()
# help(print_greeting_with_name)
# x = print_greeting_with_name('Jane')
# print(x)

# def some_of_two_numbers(a = 0, b = 0):
#     """
#
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b
#     """
#     return a + b
# x = some_of_two_numbers(25, 35)
# print(x)
# help(some_of_two_numbers)

# def is_hello_in_text(text):
#     if "hello" in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text("hello everyone"))

# def is_hello_in_text(text):
#    return "hello" in text.lower()
#
#
# print(is_hello_in_text("hello everyone"))

# def is_string_in_text(string, text):
#     return string in text
#
#
# print(is_string_in_text('he', 'the apple'))

# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! You look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'m never seen the creature like you')
#
#
# returned_value = greeting_depends_on_gender('Jack', 'male')
# returned_value = greeting_depends_on_gender('Jane', 'female')
# returned_value = greeting_depends_on_gender('Ja', 'mcale')

def main ():
    cat_voice('Meow!')
    cat_voice('Meow!')
    dog_voice('Woof!')
    dog_voice('Woof!')
    get_voice('Helloo')



def cat_voice(cat_voice):
    print(cat_voice)


def dog_voice(dog_voice):
    print(dog_voice)


def get_voice(voice):
    print(str(voice) + '!')


main()





