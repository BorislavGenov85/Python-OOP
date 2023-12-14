from pythonProject.python_oop.exams.python_oop_exam_8_april_2023.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"

        return f"{self.name} Secondary Service:\nRobots: {' '.join([r.name for r in self.robots])}"