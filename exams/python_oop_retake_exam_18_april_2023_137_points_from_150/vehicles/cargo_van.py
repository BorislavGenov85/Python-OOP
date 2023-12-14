from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        percents = round((mileage / self.max_mileage) * 100) - 5
        self.battery_level -= percents
