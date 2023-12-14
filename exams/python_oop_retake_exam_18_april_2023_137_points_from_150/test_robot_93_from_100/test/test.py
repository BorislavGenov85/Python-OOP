from unittest import TestCase, main

from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Robot


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("1", "Military", 10, 25.5)

    def test_if_init_is_correct(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(25.5, self.robot.price)

    def test_class_methods(self):
        allowed_categories = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.assertEqual(allowed_categories, self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_if_set_current_category(self):
        self.robot.category = 'Education'
        self.assertEqual('Education', self.robot.category)

    def test_if_category_not_allowed_raise_v_e(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test"

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_if_price_is_correct(self):
        self.robot.price = 15.5
        self.assertEqual(15.5, self.robot.price)

    def test_if_price_is_not_positive(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -5.5
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_existing_component(self):
        self.robot.hardware_upgrades.append("chip")
        self.robot.upgrade("chip", 5.5)
        self.assertEqual(f"Robot 1 was not upgraded.", self.robot.upgrade("chip", 5.5))

    def test_if_upgrade_is_done(self):
        self.robot.upgrade("chip", 5.5)
        self.assertEqual(33.75, self.robot.price)
        self.assertEqual(['chip'], self.robot.hardware_upgrades)

    def test_update_is_possible(self):
        self.assertEqual('Robot 1 was updated to version 2.5.', self.robot.update(2.5, 2))
        self.assertEqual(8, self.robot.available_capacity)

    def test_if_update_is_not_valid(self):
        self.robot.software_updates.append(2.5)
        self.assertEqual("Robot 1 was not updated.", self.robot.update(2.5, 2))

    def test_which_robot_price_is_bigger(self):
        other = Robot('2', "Education", 5, 15.5)

        self.assertEqual(f'Robot with ID 1 is more expensive than Robot with ID 2.',
                         self.robot.__gt__(other))
        other.price = 25.5
        self.assertEqual('Robot with ID 1 costs equal to Robot with ID 2.',
                         self.robot.__gt__(other))

        other.price = 35.5
        self.assertEqual('Robot with ID 1 is cheaper than Robot with ID 2.', self.robot.__gt__(other))


if __name__ == "__main__":
    main()
