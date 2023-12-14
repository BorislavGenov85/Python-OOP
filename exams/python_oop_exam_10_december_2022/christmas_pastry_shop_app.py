from pythonProject.python_oop.exams.python_oop_exam_10_december_2022.booths.open_booth import OpenBooth
from pythonProject.python_oop.exams.python_oop_exam_10_december_2022.booths.private_booth import PrivateBooth
from pythonProject.python_oop.exams.python_oop_exam_10_december_2022.delicacies.gingerbread import Gingerbread
from pythonProject.python_oop.exams.python_oop_exam_10_december_2022.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_VALID_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_VALID_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []  # [obj, ...]
        self.delicacies = []  # [obj, ...]
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        delicacy = [d for d in self.delicacies if d.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_VALID_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.DELICACY_VALID_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_VALID_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.BOOTH_VALID_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        booth.is_reserved = True

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int) -> str:
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        bill = booth.price_for_reservation + sum((delicacy.price for delicacy in booth.delicacy_orders))
        self.income += bill

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
