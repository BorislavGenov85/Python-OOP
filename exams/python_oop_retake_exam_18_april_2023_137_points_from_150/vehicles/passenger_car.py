from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.MAX_MILEAGE)

    def drive(self, mileage: float):
        percents = round((mileage / self.max_mileage) * 100)
        self.battery_level -= percents
