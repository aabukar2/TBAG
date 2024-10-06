from character import Enemy

# Test enemy
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hi, I'm Dave, and I want to eat your brains!")
dave.talk()

dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)
