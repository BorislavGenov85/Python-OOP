from pythonProject.python_oop.inheritance_exercise.need_for_speed_04.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
