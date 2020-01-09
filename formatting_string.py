# float_result = 1000 / 7
# print(float_result)
# print('The result of division is {0:10.2f}'.format(float_result))
# print('''
# {0:10.2f}{1:10.2f}{2:10.2f}
# {3:10.2f}{4:10.2f}{5:10.2f}
# {6:10.2f}{7:10.2f}{8:10.2f}
# '''.format(1.45778, 34.232352, 34.56565, 1234.23,
#            1.45778, 34.232352, 34.56565, 1234.23,
#            1.45778))

# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = f'My name is {name}. I\'m {age} years old.'
# print(name_and_age)
# print('My name is %s. I\'m %d years old.' % (name, age))
#
# week_day = "There are 7 days in a week: {sa}, {mo}, {tu}, {we}, {th}, {fr}, {st}."\
# .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday', fr = 'Friday', sa = 'Sunday', st = 'Saturday')
# print(week_day)

#f.strings

# name = 'Jack'
# age = 24
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = f'My name is {name}. I\'m {age} years old.'
# print(name_and_age)
#
# print('My name is %s. %s %d years old' % (name, "I'm", age)) # for Python 2 (deprecated for Python 3)

print('''
{0:15.4f}{1:15.4f}
{2:15.4f}{3:15.4f}
{3:15.4f}{4:15.4f}
{5:15.4f}{6:15.4f}
'''.format(1.45778, 34.232352, 34.56565, 1234.23,
           1.45778, 34.232352, 34.56565))