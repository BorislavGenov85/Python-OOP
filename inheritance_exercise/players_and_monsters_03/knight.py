from pythonProject.python_oop.inheritance_exercise.players_and_monsters_03.hero import Hero


class Knight(Hero):
    def __init__(self, name, level):
        super().__init__(name, level)
