rainbow_color = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_color)
print(type(rainbow_color))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56, 3, 3, 3]
text_tuple = ('sdfds', 'zxdf', 'werw', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777)
set_from_tuple.add('hello')

x = set_from_list.pop()
set_from_list.remove(3)
set_from_list.discard(43)
set_from_list.discard(3)
# set_from_list.remove(3)
set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x)

letters_set = set('Создайте множество при помощи функции set() '
                  'из текста, чтобы получить уникальные символы, '
                  'содержащиеся в тексте.')
print(letters_set)
print(type(letters_set))


