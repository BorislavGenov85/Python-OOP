class Player:
    default_guild = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.default_guild

    def add_skill(self, skill_name, mana_cost):
        for skill in self.skills:
            if skill == skill_name:
                return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"
        for skill, mana_cost in self.skills.items():
            result += f"\n==={skill} - {mana_cost}"

        return result
