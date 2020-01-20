import random

#
# while x >= 1:
#     print(x)
#     x -+ 1 # x = x - 1

# while x < 10:
#     print(x)
#     x += 1 # x = x + 1

# while x < 10:
#     print(x)
#     x += 2
#
# print('Next code')

# x = 0
# while x < 10:
#     print(str(x) + ' is less than 10')
#     x += 1
# else:
#     print(str(x) + ' now is not less 10')
#
# for x in range(10):
#     print(str(x) + ' is less than 10')
# else:
#     x += 1
#     print(str(x) + ' now is not less 10')

#break, continue, pass

my_list = [1, 2, 3]

# for item in my_list:
#    pass
# print('Another code')

# for item in my_list:
#    if item == 2:
#        break
#    print(item)
# print('Another code')

# for item in my_list:
#    if item == 2:
#        continue
#    print(item)
# print('Another code')

number = 0
number_list = [] # пустой список

while number != 7:
    number = random.randint(0, 10)  # значение от 0 до 10
    number_list.append(number)

print(number_list)
