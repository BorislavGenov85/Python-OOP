from pythonProject.python_oop.exams.final_exam.second_task_final_exam.second_hand_car import SecondHandCar

from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("Corolla", "Van", 100000, 1000.0)

    def test_correct_initialization(self):
        self.assertEqual("Corolla", self.car.model)
        self.assertEqual("Van", self.car.car_type)
        self.assertEqual(100000, self.car.mileage)
        self.assertEqual(1000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_set_invalid_price_raise_v_e(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.4
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_set_correct_price(self):
        self.car.price = 500
        self.assertEqual(500, self.car.price)

    def test_set_invalid_mileage_raise_v_e(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 56
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_correct_mileage(self):
        self.car.mileage = 1000
        self.assertEqual(1000, self.car.mileage)

    def test_if_promotional_price_is_bigger_than_current_price_raise_v_e(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price(self):
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(500))
        self.assertEqual(self.car.price, 500)

    def test_if_repair_is_impossible(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(600, "engine"))

    def test_correct_repair(self):
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(100, "engine"))
        self.assertEqual(1100, self.car.price)
        self.assertEqual(['engine'], self.car.repairs)

    def test_compare_different_type_of_cars(self):
        other = SecondHandCar("318", "coupe", 5000, 300.0)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car.__gt__(other))

    def test_compare_same_type_of_car(self):
        other = SecondHandCar("Sharan", "Van", 5000, 300.0)
        self.assertEqual(True, self.car.__gt__(other))
        other = SecondHandCar("Sharan", "Van", 5000, 1300.0)
        self.assertEqual(False, self.car.__gt__(other))

    def test_correct__str__(self):
        expect = """Model Corolla | Type Van | Milage 100000km
Current price: 1000.00 | Number of Repairs: 0"""
        actual = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(expect, self.car.__str__())


if __name__ == "__main__":
    main()
