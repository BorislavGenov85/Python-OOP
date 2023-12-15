from unittest import TestCase, main

from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("test name", "test type", "test sound")

    def test_correct_initialization(self):
        self.assertEqual("test name", self.mammal.name)
        self.assertEqual("test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound_return_correct_massage(self):
        result = self.mammal.make_sound()
        self.assertEqual("test name makes test sound", result)

    def test__if_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_if_info_return_correct_massage(self):
        result = self.mammal.info()
        self.assertEqual("test name is of type test type", result)



if __name__ == "__main__":
    main()
