from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.wild_cat_zoo_01.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
