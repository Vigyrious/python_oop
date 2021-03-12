class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0
    @classmethod
    def from_stars(cls, stars_count):
        return cls(name=f"{stars_count} stars Hotel")


    def add_room(self, room):
        self.rooms.append(room)


    def take_room(self, room_number, people):
        rooms = [r for r in self.rooms if r.number == room_number]
        if rooms:
            return rooms[0].take_room(people)


    def free_room(self, room_number):
        rooms = [r for r in self.rooms if r.number == room_number]
        if rooms:
            return rooms[0].free_room()



    def print_status(self):
        free_rooms = [f for f in self.rooms if not f.is_taken]
        hotel_guests = sum([f.guests for f in self.rooms if f.is_taken])
        print(f"Hotel {self.name} has {hotel_guests} total guests")
        print(f"Free rooms: {', '.join([str(p.number) for p in free_rooms])}")
        print(f"Taken rooms: {', '.join([str(p.number) for p in self.rooms if p not in free_rooms])}")



