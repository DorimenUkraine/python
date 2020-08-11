"""
Определите класс Dog, у которого есть методы bark и give_paw

bark возвращает строку "Bark!"
give_paw возвращает строку "Paw"

"""


class Dog():
    def bark(self, say):
        self.say = say
        return self.say

    def give_paw(self, say):
        self.say = say
        return self.say


dog = Dog()

dog.bark('Bark!')
dog.give_paw('Paw')
