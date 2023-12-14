from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)


