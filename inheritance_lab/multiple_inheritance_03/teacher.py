from pythonProject.python_oop.inheritance_lab.multiple_inheritance_03.employee import Employee
from pythonProject.python_oop.inheritance_lab.multiple_inheritance_03.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return  "teaching..."
