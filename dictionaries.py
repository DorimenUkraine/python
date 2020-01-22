# car_prices = {'opel':5000, 'toyota':7000, 'bmw':10000}
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 2000
# print(car_prices)
# # del car_prices
# # print(car_prices)
# car_prices.clear()
# print(car_prices)

# person = {
#     'first name': 'Jack',
#     'lat name': 'Brown',
#     'age': 43,
#     'hobbies': ['football', 'singing', 'photo'],
#     'children': {'son': 'Michael', 'daughter': 'Pamella' }
# }
#
# print(person['age'])
# print(person['hobbies'])
# hobbies = person['hobbies']
# print(hobbies[2])
# print(person['hobbies'][2])
#
# children = person['children']
# print(children['son'])
# print(person['children']['son'])
#
# person['car'] = 'Mazda'
# person['hobbies'][0] = 'basketball'
# print(person)
#
# print(person.keys())
# print(person.values())
# print(person.items())

# computer_items = {
#     'cpu_processor_type': 'FX 6-Core',
#     'cpu_processor_frequency': '3300.00',
#     'cpu_processor_core': '6',
#     'ram': '8Mb (DDR3)',
#     'graphics': 'NVidia FeForce GT 1030 2000 GDDR5',
#     'data_storage_device': 'HDD 1Tb'
# }
#
# print(computer_items)

# Перемена местам значений-ключей словаря

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse',
    }

new_e2f = {v: k for k, v in e2f.items()}

print(new_e2f)