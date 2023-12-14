from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.route import Route
from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.user import User
from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.vehicles.cargo_van import CargoVan
from pythonProject.python_oop.exams.python_oop_retake_exam_18_april_2023_137_points_from_150.vehicles.passenger_car import PassengerCar


class ManagingApp:
    CORRECT_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.CORRECT_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.CORRECT_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        routes = [r for r in self.routes if
                  r.start_point == start_point and r.end_point == end_point and r.length == length]
        if routes:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        routes = [r for r in self.routes if
                  r.start_point == start_point and r.end_point == end_point and r.length < length]
        if routes:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_for_repair = [v for v in self.vehicles if v.is_damaged]
        vehicles_for_repair = sorted(vehicles_for_repair, key=lambda v: (v.brand, v.model))

        counter = 0
        for vehicle in vehicles_for_repair:
            if counter == count:
                break
            counter += 1
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        res = "*** E-Drive-Rent ***\n"

        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        for user in sorted_users:
            res += str(user) + "\n"

        return res.strip()
