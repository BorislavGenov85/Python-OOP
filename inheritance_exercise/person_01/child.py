from pythonProject.python_oop.inheritance_exercise.person_01.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
