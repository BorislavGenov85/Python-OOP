from pythonProject.python_oop.exams.python_oop_exam_11_december_2021.car.muscle_car import MuscleCar
from pythonProject.python_oop.exams.python_oop_exam_11_december_2021.car.sports_car import SportsCar
from pythonProject.python_oop.exams.python_oop_exam_11_december_2021.driver import Driver
from pythonProject.python_oop.exams.python_oop_exam_11_december_2021.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.VALID_CAR_TYPES:
            return None

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        car = Controller.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if race:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self._find_last_added_car_of_this_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_car = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race_drivers = [d.name for d in race.drivers]
        if driver.name in race_drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        racers = sorted(race.drivers, key=lambda d: d.car.speed_limit, reverse=True)

        res = ""
        for i in range(3):
            driver = racers[i]
            driver.number_of_wins += 1
            res += f"Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.\n"

        return res.strip()

    def _find_last_added_car_of_this_type(self, value):
        for i in range(len(self.cars) - 1, -1, -1):
            if self.cars[i].__class__.__name__ == value and not self.cars[i].is_taken:
                return self.cars[i]
        return None
