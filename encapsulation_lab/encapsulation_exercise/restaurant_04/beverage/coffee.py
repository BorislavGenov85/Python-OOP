from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.restaurant_04.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
