import sys
from character import Character, Enemy, Friend
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

# New room for Task 4
garden = Room("Garden")
garden.set_description("A beautiful garden filled with colorful flowers and butterflies.")

# Link rooms (Including the new garden)
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(forest, "north")
forest.link_room(ballroom, "south")
garden.link_room(forest, "west")
forest.link_room(garden, "east")

# Initialize characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave, and I want to eat your brains!")
dave.set_weakness("cheese")

goblin = Enemy("Goblin", "A small and sneaky goblin.")
goblin.set_conversation("You look rich! I might let you pass if you bribe me.")
goblin.set_weakness("gold coin")

# New friendly character for Task 4
ally = Friend("Ally the Elf", "A friendly elf who loves helping adventurers.")
ally.set_conversation("Hello there! I'm Ally. Would you like a hug?")

# Add characters to rooms
dining_hall.set_character(dave)
forest.set_character(goblin)
garden.set_character(ally)

# Game loop starting in the kitchen
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    # Movement commands
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    # Talk command
    elif command == "talk":
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.talk()  # Talk to the character
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

    else:
        print("I don't know how to " + command + ".")

