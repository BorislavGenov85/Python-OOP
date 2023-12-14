from pythonProject.python_oop.exams.python_oop_exam_10_december_2022.booths.booth import Booth


class PrivateBooth(Booth):

    @property
    def reservation_price(self):
        return 3.5

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        money = number_of_people * self.reservation_price

        self.price_for_reservation = money
        self.is_reserved = True
