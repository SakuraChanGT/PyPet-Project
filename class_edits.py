from pip._vendor.distlib.compat import raw_input
import random


class Py_Pet:
    def __init__(self, name, age, photo, weight, species):
        self.name = name
        self.age = age
        self.photo = photo
        self.weight = weight    #pounds
        self.species = species
        self.household = household

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_photo(self):
        return self.photo

    def get_weight(self):
        return self.weight

    def get_species(self):
        return self.species

    def get_household(self):
        return self.household

class Pet_list:
    def __init__(self, name, max_pets):
        self.name = name
        self.max_pets = max_pets
        self.Py_Pet = []

    def add_pet(self, Py_Pet):
        if len(self.Py_Pet) <self.max_pets:
            self.Py_Pet.append(Py_Pet)
            return print("Your pet has joined the home!")
        return print("There is not enough room for this pet.")

    def get_household(self):
        value = 0
        for Py_Pet in self.Py_Pet:
            value += self.get_household


pet1 = Py_Pet("Bisco", 1, "<:3}~~~", .8, "Rat")
pet2 = Py_Pet("Freya", 2, "~=[,,_,,]:3", 13, "Cat")
pet3 = Py_Pet("Ingrid", 2, "~=[,,___,,]:3", 7, "Cat")




def startup_pypet():
    print("Welcome to Pypet!")
    commands_list()
    print("Which PyPet would you like to interact with?")
    print(pet1.name, pet2.name)

def commands_list():
    print("You can interact with your PyPet's with a few commands listed below.")
    print(" '>select pet [name]' "
          " '>stats' "
          " '>pet' "
          " '>feed' "
          " '>water' "
          " '>chat' "
          " '>play' "
          " '>rest' ")

startup_pypet()

terminate = False

while not terminate:
    print("------------------")

    user_input = raw_input('> ')

    if user_input == "quit":
        terminate = True

    elif user_input == str("select pet" + Py_Pet.get_name()):
        print("You selected" + Py_Pet.get_name(), ".")

    elif user_input == "stats":
        pypet_stats()

    elif user_input == "feed":
        print("Your PyPet nibbles on the food you offer it.")
        Py_Pet['weight'] = Py_Pet['weight'] + .15
        Py_Pet['hungry'] = False

    elif user_input == "water":
        print("Your PyPet happily drinks the water you provide.")
        Py_Pet['weight'] = Py_Pet['weight'] + .10
        Py_Pet['thirsty'] = False

    elif user_input == "chat":
        print(random.choice(Py_Pet['user_phrases']))
        print(random.choice(Py_Pet['bisco_phrases']))

    elif user_input == "pet":
        print(" Your PyPet starts to boggle in excitement.")

    elif user_input == "play":
        print("Your Pypet is excited to play with you. What would you like to play?")
        play_activities()

    elif user_input == "practice tricks":
        print("You practice some basic tricks with Bisco, after a while they grow tired and stop playing.")
        Py_Pet['tired'] = True

    elif user_input == "pull out 'The Tube'":
        print("You pull out a crinkly tube from the closet and place it on the floor. "
              "Bisco runs through it happily until running out of energy")
        Py_Pet['tired'] = True

    elif user_input == "obstacle course":
        print("You practice some basic tricks with Bisco, after a while they grow tired and stop playing.")
        Py_Pet['tired'] = True

    elif user_input == "rest":
        print("You fluff Bisco's bed stuffing and turn off the light for Bisco to go to bed. "
              "You'll check on them in some time.")
        Py_Pet['tired'] = False
        Py_Pet['hungry'] = True
        Py_Pet['thirsty'] =True
        Py_Pet['weight'] = Py_Pet['weight'] - .25

    else:
        print("Sorry, your PyPet doesn't understand what you want it to do!")


print("Goodbye!")
