from pythonProject.python_oop.exams.python_oop_exam_14_august_2022.horse_race import HorseRace
from pythonProject.python_oop.exams.python_oop_exam_14_august_2022.horse_specification.appaloosa import Appaloosa
from pythonProject.python_oop.exams.python_oop_exam_14_august_2022.horse_specification.thoroughbred import Thoroughbred
from pythonProject.python_oop.exams.python_oop_exam_14_august_2022.jockey import Jockey


class HorseRaceApp:
    HORSE_VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSE_VALID_TYPES:
            return

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.HORSE_VALID_TYPES:
            horse = self.HORSE_VALID_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [horse_race.race_type for horse_race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse = horses[-1]
        if jockey.horse is not None:
            return f"Jockey {jockey.name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        jockeys_in_race = [j for j in horse_race.jockeys]
        if jockey in jockeys_in_race:
            return f"Jockey {jockey.name} has been already added to the {horse_race.race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey.name} added to the {horse_race.race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda h: h.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockey_name = ""
        horse_name = ""
        speed = 0
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > speed:
                jockey_name = jockey.name
                horse_name = jockey.horse.name
                speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {speed}km/h is {jockey_name}! Winner's horse: {horse_name}."
