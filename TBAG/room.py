class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked = False  # Default to unlocked

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    def get_name(self):
        return self.name

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    # Lock and unlock methods
    def set_locked(self, locked):
        self.locked = locked

    def is_locked(self):
        return self.locked

