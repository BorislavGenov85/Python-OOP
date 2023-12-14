from pythonProject.python_oop.inheritance_exercise.zoo_02.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
