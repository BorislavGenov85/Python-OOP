from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.WEIGHT)

    def eating(self):
        self.weight += 1

