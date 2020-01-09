# Immutable

first_name = 'Jake'
print(first_name[2])

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1]
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

# Concatenable

yummi = "Yam"
print(yummi * 2)
print(yummi.upper())
print(yummi.lower())
print(yummi)

long_string = 'This is a long string'
print(long_string.split('s'))

str_z = "z"
new_str_zzzzzzz = str_z * 7
print(new_str_zzzzzzz)
print(new_str_zzzzzzz.upper())