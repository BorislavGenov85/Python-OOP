from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.robots.female_robot import FemaleRobot
from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.robots.male_robot import MaleRobot
from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.services.main_service import MainService
from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_VALID_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    ROBOT_SERVICES = {"MaleRobot": MainService, "FemaleRobot": SecondaryService}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.SERVICE_VALID_TYPES:
            raise Exception("Invalid service type!")

        service = RobotsManagingApp.SERVICE_VALID_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = RobotsManagingApp.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))
        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service.name} is {total_price:.2f}."

    def __str__(self):
        res = ""
        for service in self.services:
            res += service.details() + "\n"

        return res.strip()

