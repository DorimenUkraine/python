# class Car:
#
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# opel_car = Car('Opel Tigra', 'grey', '1999', is_crashed=True)
# opel_car.drive('London')
# mazda_car = Car('Mazda CX7', 'black', '2014', False)
# mazda_car.drive('Paris')
# mazda_car.change_color('yellow')
# print(mazda_car.color)
# print(opel_car.wheels_number)
# print(opel_car.name)
# print(opel_car.color)
# print(opel_car.year)
# print(opel_car.is_crashed)


# class Circle:
#
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#         self.circumference = 2 * Circle.pi * self.radius # Circle.pi - тоже самое, что и self.pi
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
#
#     # def get_circumference(self):
#     #     return 2 * self.pi * self.radius
#
# circle_1 = Circle()
# print(circle_1.get_area())
# # print(circle_1.get_circumference())
# print(circle_1.circumference)
#
# # circle_2 = Circle(3)
# # print(circle_2.get_area())
# # print(circle_2.get_circumference())
# #
# # circle_3 = Circle(5)
# # circle_area = circle_3.get_area()
# # get_circumference = circle_3.get_circumference()
# # print(circle_area)
# # print(get_circumference)

# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance
#
#     def add(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#
# account_1 = BankAccount(1, 'John', 'Brown')
# account_2 = BankAccount(2, 'Jim', 'White')
#
# account_1.add(1000)
# print(account_1.balance)
# account_1.withdraw(500)
# print(account_1.balance)
# print(account_2.balance)

class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)


    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can')
        else:
            print('You can\'t')


# print(Gamer.active_gamers)
# gamer_1 = Gamer('hell_boy', 23, 5, 13)
# print(Gamer.active_gamers)
# gamer_2 = Gamer('harry_potter', 13, 7, 34)
#
# print(gamer_1.get_age())
# gamer_1.get_adult_level_permission()
#
# print(gamer_2.get_age())
# gamer_2.get_adult_level_permission()
#
# print(Gamer.active_gamers)
#
# gamer_1.logout()
# print(Gamer.active_gamers)
# print(Gamer.get_active_gamers())

# james = Gamer.gamer_from_string('James, 34, 2, 45')
# jane = Gamer.gamer_from_string('Jane, 24, 3, 5')
# print(james.get_age())
# print(jane.get_level())
# print(Gamer.get_active_gamers())

my_dict = dict.fromkeys((1, 2, 3), ('something'))
print(my_dict)