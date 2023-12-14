from pythonProject.python_oop.exams.python_oop_exam_14_august_2022.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        else:
            self.speed = 120
