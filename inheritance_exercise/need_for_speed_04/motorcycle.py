from pythonProject.python_oop.inheritance_exercise.need_for_speed_04.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
