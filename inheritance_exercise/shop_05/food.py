from pythonProject.python_oop.inheritance_exercise.shop_05.product import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name, 15)

