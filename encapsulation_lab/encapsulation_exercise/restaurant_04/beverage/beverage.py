from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.restaurant_04.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters
