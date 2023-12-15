from unittest import TestCase, main

from pythonProject.python_oop.exams.final_exam.second_task_final_exam import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_if_initialization_is_correct(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_if_raise_error_if_hero_fight_with_himself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_raise_exception_if_hero_health_is_equal_or_smaller_than_zero(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_raise_exception_if_enemy_hero_health_is_equal_or_smaller_than_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_enemy_remove_health_after_draw(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_if_hero_win(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_if_enemy_win(self):
        self.hero.health = 20
        self.hero.damage = 20
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(35, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_if__str__method_return_correct_result(self):
        expected = f"Hero Hero: 1 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 100\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
