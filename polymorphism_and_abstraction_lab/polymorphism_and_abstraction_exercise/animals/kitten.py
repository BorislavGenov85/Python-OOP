from pythonProject.python_oop.polymorphism_and_abstraction_lab.polymorphism_and_abstraction_exercise.animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return "Meow"
