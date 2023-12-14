from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.wild_cat_zoo_01.animal import Animal


class Tiger(Animal):

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)
