from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.restaurant_04.food.food import Food


class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)