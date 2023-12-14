from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.restaurant_04.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
