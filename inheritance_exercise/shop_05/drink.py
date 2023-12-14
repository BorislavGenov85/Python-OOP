from pythonProject.python_oop.inheritance_exercise.shop_05.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, 10)

