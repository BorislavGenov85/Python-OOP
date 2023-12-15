from unittest import TestCase, main

from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_consumption_class_attribute_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_initializing_is_correct(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_drive_with_not_enough_fuel_raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_drive_car_with_enough_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(18, self.vehicle.fuel)

    def test_if_try_to_refuel_full_vehicle_tank(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_refuel_car_with_fuel(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_correct__str__method(self):
        result = str(self.vehicle)
        self.assertEqual("The vehicles has 175.5 horse power with 20.5 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()
