# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
#
# mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)
#
# print(mazda_car.name)
# print(mazda_car.is_crashed)
# print(mazda_car.wheels_number)
#
# bmw_car = Car(name='BMW', color='black', year=2018, is_crashed = False)
#
# print(bmw_car.name)
# print(bmw_car.year)
#
# number_of_wheels_of_3_cars = Car.wheels_number * 3
# print(number_of_wheels_of_3_cars)

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


blog_post_one = BlogPost(user_name='admin', text='Hello', number_of_likes=3)
blog_post_two = BlogPost(user_name='user', text='Hello. Hello.', number_of_likes=19)

blog_post_two.number_of_likes = 1000

print(blog_post_one.number_of_likes)
print(blog_post_two.number_of_likes)
