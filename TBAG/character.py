import sys
from character import Character, Enemy, Friend
from item import Item
from room import Room

# Initialize rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

forest = Room("Forest")
forest.set_description("A dark forest filled with mysterious creatures.")

garden = Room("Garden")
garden.set_description("A beautiful garden filled with colorful flowers and butterflies.")

# New room for Task 5
treasure_room = Room("Treasure Room")
treasure_room.set_description("A room filled with treasure, but the door is locked.")
treasure_room.set_locked(True)  # Start the room as locked

# Link rooms (Including the treasure room)
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(forest, "north")
forest.link_room(ballroom, "south")
garden.link_room(forest, "west")
forest.link_room(garden, "east")
treasure_room.link_room(garden, "north")
garden.link_room(treasure_room, "south")

# Initialize characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave, and I want to eat your brains!")
dave.set_weakness("cheese")

goblin = Enemy("Goblin", "A small and sneaky goblin.")
goblin.set_conversation("You look rich! I might let you pass if you bribe me.")
goblin.set_weakness("gold coin")

ally = Friend("Ally the Elf", "A friendly elf who loves helping adventurers.")
ally.set_conversation("Hello there! I'm Ally. Would you like a hug?")

# Add characters to rooms
dining_hall.set_character(dave)
forest.set_character(goblin)
garden.set_character(ally)

# Create the key item
golden_key = Item("Golden Key")
golden_key.set_description("A shiny golden key. It looks like it could open a door.")

# Place the key in the forest
forest.set_item(golden_key)

# Inventory
inventory = []

# Game loop starting in the kitchen
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    # Display current inventory
    if inventory:
        print("Inventory: " + ", ".join([item.name for item in inventory]))

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # If the room has an item, mention it
    if current_room.get_item() is not None:
        current_room.get_item().describe()

    command = input("> ")

    # Movement commands
    if command in ["north", "south", "east", "west"]:
        next_room = current_room.move(command)

        # Check if the next room is locked
        if next_room.is_locked():
            if golden_key in inventory:
                print("The door is locked, but you have the key! Use the 'unlock' command.")
            else:
                print("The door is locked. You need a key to enter.")
        else:
            current_room = next_room

    # Talk command
    elif command == "talk":
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to.")

    # Fight command (for enemies)
    elif command == "fight":
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                fight_with = input("What will you fight with? ")
                if not inhabitant.fight(fight_with):  # If fight is lost
                    print("You lost the fight!")
                    sys.exit()  # End the game if the player loses
                else:
                    print("You won the fight!")
            else:
                print("There's no one to fight here.")
        else:
            print("There is no one here to fight.")

    # Hug command for friendly characters
    elif command == "hug":
        inhabitant = current_room.get_character()
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("You can't hug this character.")

    # Give gift command for friendly characters
    elif command == "give gift":
        inhabitant = current_room.get_character()
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.give_gift()
        else:
            print("There's no one to give a gift to here.")

    # Collect item (Task 5: Collect key)
    elif command == "collect":
        item = current_room.get_item()
        if item is not None:
            inventory.append(item)
            print(f"You have collected the {item.name}.")
            current_room.set_item(None)  # Remove item from the room
        else:
            print("There is nothing to collect here.")

    # Unlock door command (Task 5)
    elif command == "unlock":
        if golden_key in inventory and current_room.get_name() == "Garden" and next_room.get_name() == "Treasure Room":
            next_room.set_locked(False)
            print("You unlocked the door to the Treasure Room!")
        else:
            print("You can't unlock anything right now.")

    else:
        print("I don't know how to " + command + ".")


