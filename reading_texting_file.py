# # Input
# x = input('Enter something')
#
# # Output
# print('Output something ' + x)
#

# lorem_ipsum_text = open('E:/Downloads/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

# lorem_ipsum_text = open('E:/Downloads/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     if 'mary' in line.lower():
#         print(line, end='')
# lorem_ipsum_text.close() # после работы с файлом в таком случае его нужно обязательно закрыть, а то он может быть поврежден

# Оператор with начиная с Python 2.6
# автоматически закрывает файл после работы с ним
# with open('E:/Downloads/sample.txt', 'r') as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'mary' in line.lower():
#             print(line, end='')

# # Вывод текста по-строчно
# with open('E:/Downloads/sample.txt', 'r') as lorem_ipsum_text:
#     # Выводится первая строка
#     line = lorem_ipsum_text.readline()
#     print(line)

# Вывод текста по-строчно
# with open('E:/Downloads/sample.txt', 'r') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     # Через цикл выведем все строки
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text.readline()

# readlines - получаем доступ ко всем строкам и формируем список. каждая строка - элемент списка
# with open('E:/Downloads/sample.txt', 'r') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line)

with open('E:/Downloads/sample.txt', 'r') as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)



