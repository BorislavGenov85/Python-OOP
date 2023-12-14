from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.restaurant_04.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)
