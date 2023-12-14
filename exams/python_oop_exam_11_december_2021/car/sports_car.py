from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, name, speed_limit):
        super().__init__(name, speed_limit)
