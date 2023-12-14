from pythonProject.python_oop.exams.python_oop_retake_exam_19_december_2022_142_from_150.band import Band
from pythonProject.python_oop.exams.python_oop_retake_exam_19_december_2022_142_from_150.band_members.drummer import Drummer
from pythonProject.python_oop.exams.python_oop_retake_exam_19_december_2022_142_from_150.band_members.guitarist import Guitarist
from pythonProject.python_oop.exams.python_oop_retake_exam_19_december_2022_142_from_150.band_members.singer import Singer
from pythonProject.python_oop.exams.python_oop_retake_exam_19_december_2022_142_from_150.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    ROCK_CONCERT_NEEDED_SKILLS = {"Drummer": "play the drums with drumsticks",
                                  "Singer": "sing high pitch notes",
                                  "Guitarist": "play rock"
                                  }
    METAL_CONCERT_NEEDED_SKILLS = {"Drummer": "play the drums with drumsticks",
                                   "Singer": "sing low pitch notes",
                                   "Guitarist": "play metal"
                                   }
    JAZZ_CONCERT_NEEDED_SKILLS = {"Drummer": "play the drums with drum brushes",
                                  "Singer": "sing high pitch notes and sing low pitch notes",
                                  "Guitarist": "play jazz"
                                  }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        self.musicians.append(ConcertTrackerApp.VALID_MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))

        band_members = {"Guitarist": 0, "Drummer": 0, "Singer": 0}
        for member in band.members:
            band_members[member.__class__.__name__] += 1

        if any(band_members.values()) < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        if not self.__check_if_band_can_play_at_concert(concert.genre, band.members):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    @staticmethod
    def __check_if_band_can_play_at_concert(genre, band_members):
        needed_skills = {
            "Rock": ConcertTrackerApp.ROCK_CONCERT_NEEDED_SKILLS,
            "Metal": ConcertTrackerApp.METAL_CONCERT_NEEDED_SKILLS,
            "Jazz": ConcertTrackerApp.JAZZ_CONCERT_NEEDED_SKILLS
        }

        for member in band_members:
            if needed_skills[genre].get(member.__class__.__name__) not in member.skills:
                return False
        return True
