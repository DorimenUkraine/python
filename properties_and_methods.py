# Immutable

first_name = "Jake"
# print(first_name[2])
# first_name[2] = 'n'

first_two_letters = first_name[:2]
print(first_two_letters)

last_letter = first_name[-1:]
print(last_letter)

#Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)



greeting = "Hello"
greeting = greeting + ' Python!'
print(greeting)

#Multiplication
yummy = "Yum"
yummy = yummy * 3
print(yummy)

print(yummy.upper())

long_string = 'This is a long string!'
print(long_string.split())

