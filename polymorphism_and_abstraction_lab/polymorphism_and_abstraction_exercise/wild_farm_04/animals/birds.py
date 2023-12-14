from pythonProject.python_oop.polymorphism_and_abstraction_lab.polymorphism_and_abstraction_exercise.wild_farm_04.animals.animal import Bird
from pythonProject.python_oop.polymorphism_and_abstraction_lab.polymorphism_and_abstraction_exercise.wild_farm_04.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Seed, Fruit]

    @property
    def gained_weight(self):
        return 0.35
