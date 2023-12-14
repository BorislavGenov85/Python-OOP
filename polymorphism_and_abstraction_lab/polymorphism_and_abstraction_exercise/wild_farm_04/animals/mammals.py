from pythonProject.python_oop.polymorphism_and_abstraction_lab.polymorphism_and_abstraction_exercise.wild_farm_04.animals.animal import Animal
from pythonProject.python_oop.polymorphism_and_abstraction_lab.polymorphism_and_abstraction_exercise.wild_farm_04.food import Fruit, Vegetable, Meat


class Mouse(Animal):

    def make_sound(self):
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Animal):

    def make_sound(self):
        return "Meow"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Animal):

    def make_sound(self):
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00
