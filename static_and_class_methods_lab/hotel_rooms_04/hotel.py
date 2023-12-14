from pythonProject.python_oop.static_and_class_methods_lab.hotel_rooms_04.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        res = room.take_room(people)
        if not res:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        guest_count = room.guests
        room.free_room()
        self.guests -= guest_count

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]
        res = f"Hotel {self.name} has {self.guests} total guests\n" \
              f"Free rooms: {', '.join([str(x.number) for x in free_rooms])}\n" \
              f"Taken rooms: {', '.join([str(x.number) for x in taken_rooms])}"
        return res
