# *args and **kwargs

# # args
# def func_with_args(*args):
#     print(args)
#
#
# func_with_args(1, 2, 3)


# def ten_percent_of_product(x, y, z):
#     return (x * y * z) * 0.1
#
# print(ten_percent_of_product(10, 20, 7))


# def ten_percent_of_product_wth_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
#
# print(ten_percent_of_product_wth_args(10, 20, 2))

# def percent_of_product_wth_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
#
# print(percent_of_product_wth_args(10, 20, 2))

# # kwargs
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
#
# func_with_kwargs(first=1, second=2, third=3)


# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
#
#
# hello_with_kwargs(gender='male', age=24, name='Lack')
# hello_with_kwargs(gender='male', age=24)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}! What is your name?'.format(greeting))
#
#
# hello_with_greeting_and_kwargs('Good morning', gender='male', age=24, name='Lack')
# # hello_with_kwargs('Hi', gender='male', age=24)

# def func_with_args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['food']))
#
#
# func_with_args_and_kwargs('one', 'two', drink='coffee', food='cendwich')


def is_cat_here(*args):
    args_in_lower_case = [str(argument).lower() for argument in list(args)]
    if 'cat' in args_in_lower_case:
        return True
    else:
        return False


print(is_cat_here('dog', 'cat', 'mouse'))


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False


print(is_cat_here(2, 3, 4))


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['color'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')


your_favorite_color('red', color='yellow')
